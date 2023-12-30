# -*- coding: UTF-8 -*-

from config import scrapper_logger
from dotenv import load_dotenv
from date_formatter import date_format
from db.article_service import ArticleService
from db.tables.max_columns_sizes import *
import json
from newspaper import Article
import url_manager
from hasher import hash_url

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

    article_map = {}
    meta_data = article3k.meta_data

    str_metadata = ""
    if (isinstance(meta_data, dict)):
        str_metadata = json.dumps(meta_data, sort_keys=True, indent=4)
    elif (isinstance(meta_data, str)):
        str_metadata = meta_data
    article_map['meta_data'] = str_metadata

    cleaned_url = url_manager.clean_url(article3k.url)
    article_map['url'] = cleaned_url
    hashed_url = hash_url(cleaned_url)

    content = article3k.text

    if (len(content) > MAX_CONTENT):
        content = article3k.text[0:MAX_CONTENT]
        scrapper_logger.warn(f"Truncated content:\t{hashed_url}\t{cleaned_url}")
    article_map['content'] = content

    section, published_time = None, None

    if (isinstance(meta_data, dict) and "article" in meta_data.keys()):

        if (isinstance(meta_data['article'], dict)):

            if ("published_time" in meta_data['article'].keys()):
                pub_time = meta_data['article']['published_time']
                published_time = date_format(pub_time)
                if (not published_time):
                    scrapper_logger.warn(f"Could not convert {pub_time}")

            if ("section" in meta_data['article'].keys()):
                section = meta_data['article']['section']
                if (type(section) == str and len(section) > MAX_SECTION):
                    section = section[0:MAX_SECTION]
                    scrapper_logger.warn(f"Truncated section:\t{hashed_url}\t{cleaned_url}")

    article_map['published_time'] = published_time
    article_map['section'] = section

    site_name, title = None, None
    if (isinstance(meta_data, dict) and "og" in meta_data.keys()):

        if (isinstance(meta_data['og'], dict)):

            if ("site_name" in meta_data['og'].keys()):

                site_name = meta_data['og']['site_name']
                if (len(site_name) > MAX_SITE_NAME):
                    site_name = site_name[0:MAX_SITE_NAME]
                    scrapper_logger.warn(f"Truncated site_name:\t{hashed_url}\t{cleaned_url}")

            if ("title" in meta_data['og'].keys()):
                title = meta_data['og']['title']
            else:
                title = article3k.title

        if (len(title) > MAX_TITLE):
            title = title[0:MAX_TITLE]
            scrapper_logger.warn(f"Truncated title:\t{hashed_url}\t{cleaned_url}")

    article_map['site_name'] = site_name
    article_map['title'] = title
    article_map['source_id'] = source_id

    keywords = None
    if (isinstance(meta_data, dict) and "keywords" in meta_data.keys()):
        keywords = meta_data['keywords']
        if (len(keywords) > MAX_KEYWORDS):
            keywords = keywords[0:MAX_KEYWORDS]
            scrapper_logger.warn(f"Truncated keywords:\t{hashed_url}\t{cleaned_url}")
    article_map['keywords'] = keywords

    authors = concat_authors(article3k.authors)
    if (len(authors) > MAX_AUTHORS):
        authors = authors[0:MAX_AUTHORS]
        scrapper_logger.warn(f"Truncated authors:\t{hashed_url}\t{cleaned_url}")

    article_map['authors'] = authors
    article_map['html'] = article3k.html

    article_map['miner'] = "zmbnews"
    return article_map

def wrap_as_json(article3k, source_id):
    """
    Wraps a newspaper3k article as a JSON
    Args:
        article3k: an instance of an newspaper.Article
        source_id: the id of the source (eg: Folha) in the database
    """
    article_map = wrap_as_map(article3k, source_id)
    return json.dumps(article_map, sort_keys=True, indent=4)

def download_n_parse(url):
    """
    Gets the article's metadata
    Args:
        url: The article's URL
    """
    article = Article(url)
    try:
        article.download()
        article.parse()
    except Exception:
        hashed_url = hash_url(url)
        scrapper_logger.error(f"Download or Parse:\t{hashed_url}\t{url}")
        return
    return article

def get_metadata(url, source_id):
    """
    Gets the article's metadata
    Args:
        url: The article's URL
    """
    article3k = download_n_parse(url)
    return wrap_as_json(article3k, source_id)

def concat_authors(lst):
    """
    Concatenate a list of authors
    """
    concatenated = ""
    n_authors = len(lst)
    sep = ", "
    k = 1
    MAX_ACCEPTABLE_NAME = 35
    for author in lst:
        author = author.strip()
        # Sometimes, newspaper3k returns authors' minibio
        if (len(author) > MAX_ACCEPTABLE_NAME):
            n_authors -= 1
            continue
        if (k == n_authors):
            sep = ""
        concatenated += author + sep
        k += 1
    return concatenated

def get_all_articles_not_sent():
    """
    Returns all articles not sent to the entities database
    """
    with ArticleService() as article_svc:
        return article_svc.read_all_articles_not_sent()

def find_article_by_id(id):
    """
    Returns an article by providing its id
    """
    with ArticleService() as article_svc:
        return article_svc.find_article_by_id(id)

def mark_article_as_sent(a_url):
    """
    Marks an article as sent in the database
    Args:
        a_url: the URL to be marked as sent
    """
    with ArticleService() as article_svc:
        return article_svc.mark_article_as_sent(a_url)
