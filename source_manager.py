# -*- coding: UTF-8 -*-

from db.source_service import SourceService

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

#add_source({'name': 'Folha de São Paulo', 'home_url': 'https://www.folha.uol.com.br', 'enabled': True})
#add_source({'name': 'Estadão', 'home_url': 'https://www.estadao.com.br/', 'enabled': True})
#add_source({'name': 'O Globo', 'home_url': 'https://oglobo.globo.com/', 'enabled': True})
