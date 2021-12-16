# -*- coding: UTF-8 -*-

from config import scrapper_logger
from db.url_service import UrlService
from db.tables.max_columns_sizes import *
from dotenv import load_dotenv
import re
from zmb_exceptions import ZmbNewsException

def has_url_been_seen(url):
    """
    Checks whether a URL has been processed before
    """
    with UrlService() as url_svc:
        return url_svc.has_url_been_seen(url)

def add_url(url):
    """
    Adds this URL to the the table tb_urls
    """
    try:
        with UrlService() as url_svc:
            url_svc.persist(url)
        return True
    except Exception as e:
        pass
    return False

def clean_url(url):
    """
    Removes the attributes of the URL
    """
    cleaned_url_lst = re.split(r'[?#]', url)
    if (len(cleaned_url_lst) == 0):
        exc_msg = f"There was a problem removing the attributes of this URL:\t{url}"
        raise ZmbNewsException(exc_msg)

    cleaned_url = cleaned_url_lst[0]
    if len(cleaned_url) > MAX_URL:
        exc_msg = f"URL too long:\t{cleaned_url}"
        raise ZmbNewsException(exc_msg)
    return cleaned_url

def identify_source_id_by_url(url):
    """
    Temporary function
    """
    if ("folha." in url):
        return 1
    elif ("estadao." in url):
        return 2
    elif("oglobo." in url):
        return 3
    else:
        return -1
