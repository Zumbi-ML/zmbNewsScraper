# -*- coding: UTF-8 -*-

import json
from db.article_service import ArticleService
from newspaper import Article

def is_url_in_db(a_url):
    """
    Checks if a URL is in the database.
    Args:
        a_url: the URL to be checked
    """
    with ArticleService() as article_svc:
        return article_svc.is_url_in_db(a_url)

def add_article(article_map):
    """
    Adds an article into the databases
    Args:
        article_map: a map that mirrors the db table
    """
    with ArticleService() as article_svc:
        article_svc.persist(article_map)

def add_all_articles(article_map_lst):
    """
    Adds a list of articles to the database
    Args:
        article_map_lst: a list of article_maps
    """
    with ArticleService() as article_svc:
        article_svc.persist_all(article_map_lst)

def wrap_as_map(article3k, source_id):
    """
    Wraps a newspaper3k article as a dictionary
    Args:
        article3k: an instance of an newspaper.Article
        source_id: the id of the source (eg: Folha) in the database
    """
    meta_data = article3k.meta_data

    article_map = {}
    article_map['uri'] = article3k.url
    article_map['content'] = article3k.text

    section, published_time = None, None

    if ("article" in meta_data.keys()):

        if ("published_time" in meta_data['article'].keys()):
            published_time = meta_data['article']['published_time']

        if ("section" in meta_data['article'].keys()):
            section = meta_data['article']['section']

    article_map['published_time'] = published_time
    article_map['section'] = section

    site_name, title = None, None
    if ("og" in meta_data.keys()):

        if ("site_name" in meta_data['og'].keys()):
            site_name = meta_data['og']['site_name']

        if ("title" in meta_data['og'].keys()):
            title = meta_data['og']['title']
        else:
            title = article3k.title

    article_map['title'] = title
    article_map['site_name'] = site_name
    article_map['source_id'] = source_id
    article_map['keywords'] = meta_data['keywords']

    return json.dumps(article_map, sort_keys=True, indent=4)

def wrap_as_json(article3k, source_id):
    """
    Wraps a newspaper3k article as a JSON
    Args:
        article3k: an instance of an newspaper.Article
        source_id: the id of the source (eg: Folha) in the database
    """
    article_map = wrap_as_map(article3k, source_id)
    return json.dumps(article_map, sort_keys=True, indent=4)

def get_article3k(url):
    """
    Gets the article's metadata
    Args:
        url: The article's URL
    """
    article = Article(url)
    article.download()
    article.parse()
    return article

def get_metadata(url, source_id):
    """
    Gets the article's metadata
    Args:
        url: The article's URL
    """
    article3k = get_article3k(url)
    return wrap_as_json(article3k, source_id)
