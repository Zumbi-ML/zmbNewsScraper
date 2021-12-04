# -*- coding: UTF-8 -*-

import config
import newspaper
from newspaper.article import ArticleException
import article_manager
import source_manager
from app.relevance_classifiers import RelevanceClassifier

def scrape_source(source_map):
    """
    Scrapes published news for the specified source
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

    articles_lst = []
    for article3k in paper.articles:
        if (not article_manager.is_url_in_db(article3k.url)):
            print("downloading: " + article3k.url)
            try:
                article3k.download()
                article3k.parse()
            except ArticleException as e:
                print("\tCould not download this article")
                continue
            articles_lst.append( \
                              article_manager.wrap_as_map(article3k, source_id))
    if (articles_lst):
        article_manager.add_all_articles(articles_lst)

def scrape_all_sources():
    """
    Scrapes published news for all enabled sources in the database
    """
    for source_map in source_manager.find_all_enabled():
        scrape_source(source_map)

scrape_all_sources()
