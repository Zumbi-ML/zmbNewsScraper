# -*- coding: UTF-8 -*-
import config
import newspaper
import article_manager
import source_manager
import url_manager
from app.relevance_classifiers import RelevanceClassifier

def wrap_unseen_url(url, source_id):
    """
    For unseen URLs, it downloads and parses an article and wraps the result as a JSON
    Args:
        url: the URL of the article
        source_id: the id of the source in the database
    """
    article_map = None
    if (not url_manager.has_url_been_seen(url)):
        # Add to a cache in the database to avoid reprocessing
        url_manager.add_url(url)

        # Download and parse URL
        article3k = article_manager.download_n_parse(url)
        if (article3k):
            article_map = article_manager.wrap_as_map(article3k, source_id)
    return article_map

def scrape_url_n_save(url, source_id):
    """
    Adds the article to the article's table if it is considered relevant
    Args:
        url: the URL of the article
        source_id: the id of the source in the database
    """
    article_map = wrap_unseen_url(url, source_id)
    if (article_map):
        if (RelevanceClassifier.is_relevant(article_map['content'])):
            article_manager.add_article(article_map)
            return True
    return False

def wrap_source(source_map):
    """
    Wraps published news for the specified source as a list of maps
    Args:
        source_map: A map in the following format:
                    {'id': 1, 'home_url': 'http://www.folha.uol.com.br'}
    """
    source_id = source_map['id']
    home_url = source_map['home_url']

    # Build a specific source home_url
    # E.g.: home_url: http://www.folha.uol.com.br
    # Read the documentation to understand the steps in building a source
    # https://newspaper.readthedocs.io/en/latest/
    paper = newspaper.Source(home_url, config.scrapper_cfg)
    paper.build()

    article_maps = []
    for article3k in paper.articles:
        article_map = wrap_unseen_url(article3k.url, source_id)
        if (article_map):
            article_maps.append(article_map)
    return article_maps

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

def scrape_all_sources_n_save():
    """
    Scrapes published news for all enabled sources in the database
    """
    success = True
    for source_map in source_manager.find_all_enabled():
        success = success and scrape_source_n_save(source_map)
    return success
