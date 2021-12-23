# -*- coding: UTF-8 -*-

import config
import pickle
import numpy as np

from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer

NOT_RELEVANT, RELEVANT = 0, 1
RELEV_THRESHOLD = 0.75

class BaseNBClf(object):
    """
    Checks whether a text is relevant for extracting entities
    """

    def __init__(self):
        """
        Constructor
        """
        self._stemmer = RSLPStemmer()

    def is_relevant(self, text):
        """
        Checks whether the text is relevant for extracting named entities
        Args:
            text: the text to be classified
        Returns:
            True: if the text is relevant
            False: if the text is NOT relevant
        """
        vectorized = self._transform(text)
        np_pred = self._model.predict(vectorized)
        return int(np_pred[0]) == RELEVANT

    def relevance(self, text):
        """
        Returns the class of the prediction (0: False, 1: True) and the
        model's confidence in the probability for each class (e.g., [0.2, 0.8])
        Args:
            text: the text to be classified
        """
        vectorized = self._transform(text)

        np_pred = self._model.predict(vectorized)
        is_relevant = int(np_pred[0]) == RELEVANT

        proba = self._model.predict_proba(vectorized)
        return is_relevant, proba[0]

    def relevance_on_threshold(self, text, threshold=RELEV_THRESHOLD):
        """
        Predicts whether a text is relevant based on both the model's prediction
        and the established threshold
        """
        vectorized = self._transform(text)

        np_pred = self._model.predict(vectorized)
        is_relev_model = int(np_pred[0]) == RELEVANT

        proba = self._model.predict_proba(vectorized)
        is_relev = is_relev_model and proba[0][1] >= RELEV_THRESHOLD
        return is_relev, proba[0]

    def _transform(self, text):
        """
        Stems and vectorizes the text
        Args:
            text: the text to be stemmed and vectorized
        """
        transformed = ""
        word_tokens = word_tokenize(text)
        for w in word_tokens:
            transformed += f"{self._stemmer.stem(w)} "
        return self._vectorizer.transform([transformed])


class MutinomialNBClf(BaseNBClf):

    def __init__(self, model_filepath=None):
        """
        Constructor
        Args:
            model_filepath: the location of the pickle model
        """
        super().__init__()
        FILE_PATH = model_filepath if model_filepath else config.MULTINOMIAL_CLF_MODEL
        with open(FILE_PATH, 'rb') as f:
            self._vectorizer, self._model = pickle.load(f)

class BernoulliNBClf(BaseNBClf):

    def __init__(self, model_filepath=None):
        """
        Constructor
        Args:
            model_filepath: the location of the pickle model
        """
        super().__init__()
        FILE_PATH = model_filepath if model_filepath else config.BERNOULLI_CLF_MODEL
        with open(FILE_PATH, 'rb') as f:
            self._vectorizer, self._model = pickle.load(f)
