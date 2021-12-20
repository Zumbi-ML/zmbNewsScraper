# -*- coding: UTF-8 -*-
from app.classifiers.relevance_classifiers import MutinomialNBClf
import argparse
import article_manager
from config import scrapper_cfg, scrapper_logger
import ner_manager
import newspaper
import source_manager
from tqdm import tqdm
import url_manager
from zmb_exceptions import ZmbNewsException
from hasher import hash_url

relevance_clf = MutinomialNBClf()

def scrape_all_sources_n_save():
    """
    Scrapes published news for all enabled sources in the database
    """
    success = True
    for source_map in tqdm(source_manager.find_all_enabled()):
        success = success and scrape_source_n_save(source_map)
    return success

def scrape_source_n_save(source_map):
    """
    Scrapes a source for published articles and adds them to the articles' table
    Args:
        source_map: A map in the following format:
                    {'id': 1, 'home_url': 'http://www.folha.uol.com.br'}
    """
    article_maps = wrap_source(source_map)
    if (article_maps):
        article_manager.add_all_articles(article_maps)
        return True
    return False

def scrape_url_n_save(url, source_id):
    """
    Adds the article to the article's table if it is considered relevant
    Args:
        url: the URL of the article
        source_id: the id of the source in the database
    """
    # Remove attributes of the URL
    # Raises an exception if the cleaning goes wrong
    cleaned_url = url_manager.clean_url(url)

    article_map = wrap_unseen_url(cleaned_url, source_id)
    if (article_map and is_relevant(article_map)):
        article_map = ner_manager.wrap_entities(article_map)
        article_manager.add_article(article_map)
        return True
    return False

def scrape_url_list_n_save(url_lst):
    """
    Adds a list of articles' URLs to the article's table if it is considered relevant
    Args:
        url_lst: a list of URLs
    """
    for url in url_lst:
        if (not url):
            continue
        try:
            source_id = source_manager.identify_source_id_by_url(url)
            if (not source_id):
                continue
            scrape_url_n_save(url, source_id)
        except ZmbNewsException as e:
            scrapper_logger.warn(f"A problem ocurred cleaning the URL: {url}")

# Helper functions
# ==============================================================================

def wrap_unseen_url(url, source_id):
    """
    For unseen CLEANED URLs, it downloads and parses an article and wraps the result as a JSON
    Args:
        url: the URL of the article
        source_id: the id of the source in the database
    """
    article_map = None

    is_new_url = not url_manager.has_url_been_seen(url)
    hashed_url = hash_url(url)

    msg = f"""New:\t{is_new_url}\t{hashed_url}\t{url}"""
    scrapper_logger.info(msg)
    print(msg)

    if (is_new_url):
        # Add to a cache in the database to avoid reprocessing
        url_manager.add_url(url)

        # Download and parse URL
        article3k = article_manager.download_n_parse(url)
        if (article3k):
            article_map = article_manager.wrap_as_map(article3k, source_id)
    return article_map

def wrap_source(source_map):
    """
    Wraps published news for the specified source as a list of maps
    Args:
        source_map: A map in the following format:
                    {'id': 1, 'home_url': 'http://www.folha.uol.com.br'}
    """
    source_id = source_map['id']
    home_url = source_map['home_url']

    msg = f"""{home_url}"""
    scrapper_logger.info(msg)
    print(msg)

    # Build a specific source home_url
    # E.g.: home_url: http://www.folha.uol.com.br
    # Read the documentation to understand the steps in building a source
    # https://newspaper.readthedocs.io/en/latest/
    paper = newspaper.Source(home_url, scrapper_cfg)
    paper.build()

    article_maps = []
    for article3k in tqdm(paper.articles):
        try:
            # Remove parameters of the URL
            cleaned_url = url_manager.clean_url(article3k.url)
        except ZmbNewsException as e:
            scrapper_logger.warn(str(e))
            continue

        article_map = wrap_unseen_url(cleaned_url, source_id)
        if (article_map and is_relevant(article_map)):
            article_map = ner_manager.wrap_entities(article_map)
            article_maps.append(article_map)
    return article_maps

def is_relevant(article_map):
    """
    Checks whether an article_map is relevant
    Args:
        article_map: a dictionary representing the article
    """
    is_relevant = relevance_clf.is_relevant(article_map['content'])

    # Logging
    url = article_map['url']
    hashed_url = hash_url(url)
    msg = f"""Relevant:\t{is_relevant}\t{hashed_url}\t{url}"""
    scrapper_logger.info(msg)
    print(msg)

    return is_relevant
