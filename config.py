# -*- coding: UTF-8 -*-

from newspaper import Config
from datetime import date
import os
import logging
import spacy
import pt_zmbner

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

# Loggers
# ==============================================================================

LOGS_DIR = '/logs'
LOGS_FILE_EXT = '.log'

def get_logger(appname):
    """
    Obtains a logger
    Args:
        appname: the name of the app to be logged
    """
    log_dir_path = os.path.dirname(os.path.realpath(__file__)) + LOGS_DIR
    log_filename = date.today().strftime(f"{appname}_%Y-%m-%d") + LOGS_FILE_EXT
    log_full_filename = os.path.join(log_dir_path, log_filename)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_full_filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s'))
    logger.addHandler(file_handler)
    return logger

scrapper_logger = get_logger("scrapper")
sender_logger = get_logger("sender")
