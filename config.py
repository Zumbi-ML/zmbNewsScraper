# -*- coding: UTF-8 -*-

from newspaper import Config
from datetime import date
import os
import logging
import spacy
import pt_zmbner
from zmb_loggers import get_logger

# NER Extractor
# ==============================================================================

nlp = pt_zmbner.load()

# Scraper
# ==============================================================================
SCRAPER_LANGUAGE = 'pt'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

scrapper_cfg = Config()
scrapper_cfg.browser_user_agent = USER_AGENT
scrapper_cfg.request_timeout = 10
scrapper_cfg.memoize_articles = False


# RelevanceClassifier
# ==============================================================================

RELEV_CLF_DIR = "app/classifiers/"

MULTINOMIAL_CLF_MODEL = RELEV_CLF_DIR + "multinomial_nb_clf.pkl"
BERNOULLI_CLF_MODEL = RELEV_CLF_DIR + "bernoulli_nb_clf.pkl"

# Loggers
# ==============================================================================

scrapper_logger = get_logger("scrapper", enum_each_exec=True)
sender_logger = get_logger("sender", enum_each_exec=True)
date_formatter = get_logger("date_formatter", enum_each_exec=False)

# Relevant URLs
# ==============================================================================
DATA_DIR = "data/"

RELEVANT_URLs_DIR = DATA_DIR + "URLs/"

RELEVANT_URLs_FILE = RELEVANT_URLs_DIR + "relevant-URLs.tsv"
