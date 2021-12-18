# -*- coding: UTF-8 -*-

import config
import pickle
import numpy as np

NOT_RELEVANT, RELEVANT = 0, 1

class MutinomialNBClf(object):
    """
    Checks whether a text is relevant for extracting entities
    """

    def __init__(self, model=config.RELEV_CLF_MODEL):
        """
        Constructor
        Args:
            model: the location of the pickle model
        """
        with open(model, 'rb') as f:
            self._vectorizer, self._model = pickle.load(f)

    def is_relevant(self, text):
        """
        Checks whether the text is relevant for extracting named entities
        Args:
            text: the text to be classified
        Returns:
            True: if the text is relevant
            False: if the text is NOT relevant
        """
        vectorized = self._vectorizer.transform([text])
        np_pred = self._model.predict(vectorized)
        return  int(np_pred[0]) == RELEVANT
