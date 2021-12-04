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

    def persist_all(self, home_urls):
        """
        Persists all URLs in the database
        Args:
            home_urls: a list of news sites home URLs.
            E.g.: http://folha.uol.com.br
        """
        for url in home_urls:
            source = TableSources( \
                home_url=url,
                enabled=True,
            )
            self._session.add(source)
