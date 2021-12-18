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

def get_domain(url):
    """
    Returns the domain (and subdomain) of the URL
    """
    url = url.lower()
    # Remove scheme
    cleaned_url = re.sub(r"https?://", "", url)
    # Remove subdomain
    cleaned_url = re.sub(r"www\d?\d?\.", "", cleaned_url)

    # Split by top level domain
    if (".com" in cleaned_url):
        sep = ".com"
    elif (".gov" in cleaned_url):
        sep = ".gov"
    elif (".edu" in cleaned_url):
        sep = ".edu"
    elif (".leg" in cleaned_url):
        sep = ".leg"
    elif (".mil" in cleaned_url):
        sep = ".mil"
    elif (".jus" in cleaned_url):
        sep = ".jus"
    elif (".org" in cleaned_url):
        sep = ".org"
    elif (".inf" in cleaned_url):
        sep = ".inf"
    elif (".br" in cleaned_url):
        sep = ".br"
    elif (".pt" in cleaned_url):
        sep = ".pt"
    else:
        return None

    parts = cleaned_url.split(sep)
    the_domain = None
    if (len(parts) > 0):
        the_domain = parts[0]
    return the_domain
