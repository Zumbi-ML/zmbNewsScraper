# -*- coding: UTF-8 -*-


DISCRIMINATIVE_TERMS = \
    ['racismo',
     #'ativismo',
     #'polícia',
     'negro',
     'negra',
     'racial',
     #'brutalidade',
     #'militante',
     'afro',
     #'violência',
     'crime',
     #'estrutural',
     'raça',
     'preconceito',
     'cor',
     'etnia',
     'injúria',
     'minoria',
     'discriminação',
     #'depreciação',
     'macaco',
     #'movimento',
     #'branco',
     'preto',
     'igualdade',
     'consciência',
     #'inclusão',
     'racista',
     'branquitude',
     'miscigenação',
     'miscigenado',
     'pardo',
     'parda',
     #'índio',
     'supremacia',
     #'nazismo',
     #'desigualdade',
     #'desigual',
     'africano',
     'áfrica',
     'afrodescendente']

class RelevanceClassifier(object):
    """
    Checks whether a text is relevant for extracting entities
    """

    def is_relevant(text):
        """
        Checks whether the text is relevant for extracting named entities
        """
        for term in DISCRIMINATIVE_TERMS:
            enveloped = f" {term} "
            if enveloped in text.lower():
                return True
        return False
