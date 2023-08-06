import torch

from TakeBlipNer.predict import NerPredict
from TakeBlipPosTagger.predict import PosTaggerPredict
from TakeBlipNer.utils import load_fasttext_embeddings


def load_postagging_predictor(postagging_model_path: str,
                              postagging_label_path: str,
                              embedding_path: str) -> PosTaggerPredict:
    """
    Parameters
    ----------
    postagging_model_path : str
            path to the postagging model
    postagging_label_path : str
            path to the labels dictionary of postag model
    embedding_path : str
            path to embedding model

    Returns
    -------
    PosTaggerPredict
        Return object to predict the postag labels
    """
    embedding = load_fasttext_embeddings(embedding_path, '<pad>')
    postag_model = torch.load(postagging_model_path)
    postag_predictor = PosTaggerPredict(
        model=postag_model,
        label_path=postagging_label_path,
        embedding=embedding
    )
    return postag_predictor


def load_ner_predictor(ner_model_path: str, ner_label_path: str,
                       postag_predictor: PosTaggerPredict) -> NerPredict:
    """
    Parameters
    ---------
    ner_model_path : str
            path to the ner model
    ner_label_path : str
            path to the labels dictionary of ner model
    postag_predictor : PosTaggerPredict
            Object to predict the postag labels

    Returns
    -------
    NerPredict
        Return object to predict the ner labels
    """
    ner_model = torch.load(ner_model_path)
    ner_predictor = NerPredict(
        model=ner_model,
        label_path=ner_label_path,
        postag_model=postag_predictor,
        pad_string='<pad>',
        unk_string='<unk>'
    )
    return ner_predictor
