# -*- coding: UTF-8 -*-

from db.url_service import UrlService

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
