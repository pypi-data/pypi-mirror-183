import csv
from typing import Optional, List
from TakeBlipInsightExtractor.outputs.eventhub_log_sender import \
    EventHubLogSender
from TakeBlipMessageStructurer.predict import MessageStructurer
from take_text_preprocess.presentation import pre_process
from TakeBlipInsightExtractor.inputs.datalake_connector import DatabricksConnector

class DataGenerator:
    def __init__(self, data, separator):
        self.data = data
        self.separator = separator

    @classmethod
    def from_multipart_data_request(cls, part_data, encoding, separator):
        file_part_data = part_data.text.splitlines()
        return cls(file_part_data, separator)

    @classmethod
    def from_file_data(cls, path, encoding, separator):
        file_handler = open(path, encoding=encoding)
        return cls(file_handler, separator)

    def iterate_data(self):
        csv_reader = csv.reader(self.data, delimiter=self.separator)
        for row in csv_reader:
            yield row


class OutputFile:

    def __init__(self, input_data, encoding, separator, data_from='request',
                 logger=None, datalake_connector=None):
        """
        Parameters
        ----------
        input_data : str
            path to the csv file to be analyzed
        encoding : str
            file encoding
        separator : str
            csv file delimiter character
        data_from : str
            string to indicate if the file is from a request or local
        logger : EventHubLogSender
            event hub logger
        datalake_connector : DatabricksConnector
            datalake connector to receive messages from datalake
        """
        self.__messages_list = None
        self.input_data = input_data
        self.encoding = encoding
        self.separator = separator
        self.__logger = logger
        self.__datalake_connector = datalake_connector
        self.get_data = self.get_data_function(data_from)
        self.__set_header()

    def get_data_function(self, data_from):
        if data_from == 'request':
            return self.get_data_from_request
        elif data_from == 'file':
            return self.get_data_from_file
        elif data_from == 'datalake':
            return self.get_data_from_datalake
        else:
            raise Exception('Data origin not accepted')

    def get_data_from_file(self):
        return DataGenerator.from_file_data(
            path=self.input_data,
            encoding=self.encoding,
            separator=self.separator
        ).iterate_data()

    def get_data_from_request(self):
        return DataGenerator.from_multipart_data_request(
            part_data=self.input_data,
            encoding=self.encoding,
            separator=self.separator
        ).iterate_data()

    def get_data_from_datalake(self):
        messages = self.__datalake_connector.consume_data()
        return messages

    def __set_header(self):
        self.header = ['Mensagens', 'Tópicos', 'Assuntos']

    def parse_message_structurer_content(self, structured_messages_list: list) \
            -> (list, list):
        """Generate the column with the filtered messages and the entities

        Parameters
        ----------
        structured_messages_list : list
            List with structured message (with entities and filtered_message)
            of each row.

        Returns
        -------
        (list, list)
            List with the filtered message of each row, and list with entities
            of each row.
        """
        filtered_message_column = []
        entities_column = []
        for structured_message in structured_messages_list:
            filtered_message_column.append(
                structured_message['lowercase_filtered_message'])
            content = structured_message['content']
            if len(content) > 0:
                entities_list = [tag for tag in content
                                 if tag['type'] != 'postagging']
            else:
                entities_list = []
            entities_column.append(entities_list)
        return filtered_message_column, entities_column

    def __get_messages_list(self):
        return self.__messages_list

    def create_message_structurer_columns(self, batch_size: int,
                                          message_structurer: MessageStructurer,
                                          tags_to_remove: list,
                                          messages: Optional[List[str]]=None) -> (list, list):
        """
        Parameters
        ----------
        batch_size : int
            size of each batch to the prediction
        message_structurer : MessageStructurer
            message structurer model
        tags_to_remove : list
            list with tags to be removed in the message structurer

        Returns
        -------
        (list, list)
            List with the filtered message of each row, and list with entities
            of each row.

        Args:
            messages:
        """

        if messages:
            self.__messages_list = messages
            self.get_data = self.__get_messages_list

        ms_input_batch = [{'id': ind, 'sentence': pre_process(row[0],
                                                              ["URL", "EMAIL", "NUMBER", "CODE", "SYMBOL", "EMOJI"])}
                          for ind, row in enumerate(self.get_data())]

        self.log_message('DEBUG', 'Number of messages sent to be '
                                  'structured {}.'
                         .format(len(ms_input_batch)))
        self.log_message('DEBUG', 'Maximum message size {}'
                         .format(max(len(message['sentence'].split())
                                     for message in ms_input_batch)))

        structured_messages_list = sorted(
            message_structurer.structure_message_batch(
                batch_size=batch_size,
                sentences=ms_input_batch,
                tags_to_remove=tags_to_remove,
                use_pre_processing=False
            ),
            key=lambda content_dict: content_dict['id']
        )
        self.log_message('DEBUG', 'Messages structured with success.')
        filtered_message_column, entities_column = \
            self.parse_message_structurer_content(structured_messages_list)
        return filtered_message_column, entities_column

    def log_message(self, level, message):
        if self.__logger:
            self.__logger.log_message(level, message)

    @staticmethod
    def create_groups_column(entities_column: list,
                             parent_entity_dict: dict) -> list:
        """
        Parameters
        ----------
        entities_column : list
            list with entities of each row
        parent_entity_dict: dict
            dictionary with the relation parent - entities

        Returns
        -------
        list
            List with the name of the group of each entity of each row.
        """
        group_column = []
        entity_parent_dict = {child: parent for parent, children_lst in
                              parent_entity_dict.items() for child in
                              children_lst}

        for entities_list in entities_column:
            temp_list = []
            for entity_dict in entities_list:
                entity_name = entity_dict['lowercase_value']
                parent = entity_parent_dict[entity_name]
                temp_list.append(parent)
            group_column.append(temp_list)
        return group_column

    def create_messages_frequency_dict(self, entities_column: list) \
            -> dict:
        """
        Create a dictionary with the entities of a sentence as key and list
        with all sentences that has this entity, and their frequency as values.

        Parameters
        ----------
        entities_column : list
            list with entities of each row

        Returns
        -------
        dict
            Dictionary withe the entity as key and a list with a tuple of
            a sentence and the frequency as values.
        """
        messages_frequency_dict = {}
        entity_message_dict = {}
        for row in self.get_data():
            message = row[0]
            messages_frequency_dict[message] = messages_frequency_dict.get(
                message, 0) + 1

        for row, entities_list in zip(self.get_data(),
                                      entities_column):
            message = row[0]
            for entity_dict in entities_list:
                entity_name = entity_dict['lowercase_value']
                if entity_message_dict.get(entity_name) is not None:
                    entity_message_dict[entity_name].append((message,
                                                             messages_frequency_dict[
                                                                 message]))
                    entity_message_dict[entity_name] = list(
                        set(entity_message_dict[entity_name]))
                else:
                    entity_message_dict[entity_name] = [(
                        message, messages_frequency_dict[
                            message])]
        return entity_message_dict

    def __generate_output_file(self, entities_column: list, group_column: list):
        """
        Generate each output row

        Parameters
        ----------
        entities_column : list
            list with entities of each row
        group_column : list
            List with the name of the group of each entity of each row.
        """
        for message, entity_dict, group in zip(
                self.get_data(),
                entities_column,
                group_column):
            if len(entity_dict) > 0:
                entity_list = [entity['lowercase_value'] for entity in
                               entity_dict]
            else:
                entity_list = []
            yield message[0], entity_list, group

    def save_output_file(self, full_path: str,
                         entities_column: list,
                         group_column: list):
        """
        Save csv file with the original message, the filtered message, the
        entities found and the groups of the entities.

        Parameters
        ----------
        full_path : str
            String with the path to save the file
        entities_column : list
            list with entities of each row
        group_column : list
            List with the name of the group of each entity of each row.
        """
        with open(full_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=self.separator)
            if self.header:
                writer.writerow(self.header)
            for row in self.__generate_output_file(entities_column,
                                                   group_column):
                writer.writerow(row)
