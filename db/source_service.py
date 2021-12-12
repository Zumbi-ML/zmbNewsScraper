# -*- coding: UTF-8 -*-

from .base_service import BaseService
from db.tables.tb_definitions import *

class SourceService(BaseService):
    """
    Is in charge of managing the database session for larger tasks
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def find_all_enabled(self):
        """
        Finds all enabled news sources
        """
        results = self._session.query(TableSources) \
                                        .filter(TableSources.enabled == 1).all()

        home_urls = []
        for row in results:
            home_urls.append({"id": row.id, "home_url": row.home_url})
        return home_urls

    def persist(self, source_map):
        """
        Adds a source_map into the session
        Args:
            source_map: a map mirroring the table sources.
            E.g.:
                {'name': Folha de S. Paulo',
                 'url': 'http://folha.uol.com.br',
                 'enabled': True,}
        """
        source = TableSources( \
            name=source_map['name'],
            home_url=source_map['home_url'],
            enabled=source_map['enabled'],
        )
        self._session.add(source)


    def persist_all(self, source_map_lst):
        """
        Adds a list of source_maps into the session
        Args:
            source_map_lst: a list of source_maps.
                            See the method persist for an example of source_map.
        """
        for source_map in source_map_lst:
            self.persist(source_map)
