# -*- coding: UTF-8 -*-

from services.source_service import SourceService
from dotenv import load_dotenv
import managers.url_manager as url_manager

def add_sources(source_map_lst):
    """
    Adds a list of sources into the database
    """
    with SourceService() as source_svc:
        source_svc.persist_all(source_map_lst)

def add_source(source_map):
    """
    Add a source map into the database
    """
    with SourceService() as source_svc:
        source_svc.persist(source_map)

def find_all_enabled():
    """
    Returns all news sources recorded into the database
    """
    all_sources = None
    with SourceService() as source_svc:
        all_sources = source_svc.find_all_enabled()
    return all_sources

def find_name_by_id(id):
    """
    Return the name of the source by id
    """
    with SourceService() as source_svc:
        return source_svc.find_name_by_id(id)

def identify_source_id_by_url(url):
    """
    Identifies the source id for a given URL
    """
    url_key = url_manager.get_domain(url)
    if (not url_key):
        return None

    with SourceService() as source_svc:
        return source_svc.find_source_id_by_url_key(url_key)
