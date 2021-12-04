# -*- coding: UTF-8 -*-

from db.source_service import SourceService

def add_source(sources_lst):
    """
    Adds a list of sources into the database
    """
    with SourceService() as source_svc:
        source_svc.persist_all(sources_lst)

def find_all_enabled():
    """
    Returns all news sources recorded into the database
    """
    all_sources = None
    with SourceService() as source_svc:
        all_sources = source_svc.find_all_enabled()
    return all_sources

#add_source(['http://www.folha.uol.com.br'])

# Main
# ==============================================================================

#if (__name__ == '__main__'):
#    all = find_all_enabled()
#    print(all)
