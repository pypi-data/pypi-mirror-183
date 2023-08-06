import os
import re
import ast


def get_ie_static_parameters():
    return {
        'node_messages_examples': get_node_messages_examples(),
        'similarity_threshold': get_similarity_threshold(),
        'percentage_threshold': get_percentage_threshold(),
        'batch_size': get_batch_size(),
        'chunk_size': get_chunk_size(),
        'embedding_path': get_embedding_path(),
        'postagging_model_path': get_postagging_model_path(),
        'postagging_label_path': get_postagging_label_path(),
        'ner_model_path': get_ner_model_path(),
        'ner_label_path': get_ner_label_path(),
        'eventhub_name': get_eventhub_name(),
        'application_name': get_application_name(),
        'server_host_name': get_server_host_name(),
        'http_path': get_http_path(),
        'access_token': get_access_token(),
        'message_column': get_message_column(),
        'storage_date_column': get_storage_date_column(),
        'identity_column': get_identity_column(),
        'data_table': get_data_table(),
        'message_id_column': get_message_id_column(),
        'subject_data_table': get_subject_data_table(),
        'subject_bot_name_column': get_subject_bot_name_column(),
        'subject_message_id_column': get_subject_message_id_column(),
        'use_neighborhood': get_use_neighborhood()
    }


def get_embedding_path():
    return get_azureml_file_path(
        env_model_name='EMBEDDING_VERSION',
        env_full_name='EMBEDDING_FULL_NAME',
        env_registry_name='EMBEDDING_REGISTRY_NAME'
    )


def get_postagging_model_path():
    return get_azureml_file_path(
        env_model_name='POSTAGGING_VERSION',
        env_full_name='POSTAGGING_FULL_NAME',
        env_registry_name='POSTAGGING_REGISTRY_NAME'
    )


def get_postagging_label_path():
    return get_azureml_file_path(
        env_model_name='POSTAGGING_LABEL_VERSION',
        env_full_name='POSTAGGING_LABEL_FULL_NAME',
        env_registry_name='POSTAGGING_LABEL_REGISTRY_NAME'
    )


def get_ner_model_path():
    return get_azureml_file_path(
        env_model_name='NER_VERSION',
        env_full_name='NER_FULL_NAME',
        env_registry_name='NER_REGISTRY_NAME'
    )


def get_ner_label_path():
    return get_azureml_file_path(
        env_model_name='NER_LABEL_VERSION',
        env_full_name='NER_LABEL_FULL_NAME',
        env_registry_name='NER_LABEL_REGISTRY_NAME'
    )


def get_azureml_file_path(env_model_name, env_full_name, env_registry_name):
    azureml_dir = os.environ.get('AZUREML_MODEL_DIR')
    file_version = os.environ.get(env_model_name)
    file_full_name = os.environ.get(env_full_name)
    file_registry_name = os.environ.get(env_registry_name)
    return os.path.join(
        azureml_dir,
        file_registry_name,
        file_version,
        file_full_name
    )


def get_node_messages_examples():
    return int(os.environ.get('NUMBER_NODE_MESSAGES_EXAMPLES', 6))


def get_similarity_threshold():
    return float(os.environ.get('SIMILARITY_THRESHOLD', 0.65))


def get_percentage_threshold():
    return float(os.environ.get('PERCENTAGE_THRESHOLD', 0.7))


def get_batch_size():
    return int(os.environ.get('BATCH_SIZE', 50))


def get_chunk_size():
    return int(os.environ.get('CHUNK_SIZE', 1024))


def get_environment():
    return os.environ.get('ENVIRONMENT', 'prod')


def get_eventhub_name():
    return os.environ.get('EVENTHUB_NAME', None)


def get_application_name():
    return os.environ.get('APPLICATION_NAME', None)


def get_server_host_name():
    return os.environ.get('SERVER_HOSTNAME', None)


def get_http_path():
    return os.environ.get('HTTP_PATH', None)


def get_access_token():
    return os.environ.get('ACCESS_TOKEN', None)


def get_message_column():
    return os.environ.get('MESSAGE_COLUMN', None)


def get_storage_date_column():
    return os.environ.get('STORAGE_DATE_COLUMN', None)


def get_identity_column():
    return os.environ.get('IDENTITY_COLUMN', None)


def get_data_table():
    return os.environ.get('DATA_TABLE', None)


def get_message_id_column():
    return os.environ.get('MESSAGE_ID_COLUMN', None)


def get_subject_data_table():
    return os.environ.get('SUBJECT_DATA_TABLE', None)


def get_subject_bot_name_column():
    return os.environ.get('SUBJECT_BOT_NAME_COLUMN', None)


def get_subject_message_id_column():
    return os.environ.get('SUBJECT_MESSAGE_ID_COLUMN', None)

def get_use_neighborhood():
    return os.environ.get('USE_NEIGHBORHOOD', True)

def get_parameters_for_multipart_request(multipart_data):
    parameters = {
        'separator': '|',
        'file_name': 'file.csv',
        'bot_name': None,
        'user_email': None,
        'file': None,
    }
    for part in multipart_data.parts:
        disposition = part.headers[b'Content-Disposition'].decode('utf-8')
        parameter_name = re.search('name="(.*?)"', disposition.split(';')[1]).group(1)
        if parameter_name == 'bot_name':
            parameters['bot_name'] = part.text
        elif parameter_name == 'user_email':
            parameters['user_email'] = part.text
        elif parameter_name == 'separator':
            parameters['separator'] = part.text
        elif parameter_name == 'file':
            parameters['file'] = part
            parameters['file_name'] = re.search('filename="(.*?)"', disposition.split(';')[2]).group(1)
    return parameters


def check_parameters(parameters):
    for parameter_name in parameters:
        if not parameter_name:
            raise ValueError('Missing {} parameter in form data request'.format(parameter_name))


def get_parameters_for_json_request(request):
    parameters = {
        'bot_name': None,
        'user_email': None,
        'start_date': None,
        'end_date': None,
        'bot_identity': None,
        'separator': '|',
        'file_name': 'file.csv',
        'file': None,
    }

    dict_str = request.decode("UTF-8")
    request_data = ast.literal_eval(dict_str)

    for parameter_name in request_data.keys():
        if parameter_name == 'bot_name':
            parameters[parameter_name] = request_data[parameter_name]
        elif parameter_name == 'user_email':
            parameters[parameter_name] = request_data[parameter_name]
        elif parameter_name == 'start_date':
            parameters[parameter_name] = request_data[parameter_name]
        elif parameter_name == 'end_date':
            parameters[parameter_name] = request_data[parameter_name]
        elif parameter_name == 'bot_identity':
            parameters[parameter_name] = request_data[parameter_name]

    return parameters
