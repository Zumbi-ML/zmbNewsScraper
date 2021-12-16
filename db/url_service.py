# -*- coding: UTF-8 -*-

from .base_service import BaseService
from db.tables.tb_definitions import *
from datetime import date

class UrlService(BaseService):

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def has_url_been_seen(self, a_url):
        """
        Checks whether a given URL
        Args:
            a_url: a news article URL
        """
        hashed_url = hash(a_url)
        result = self._session.query(TableURL) \
                           .filter(TableURL.hashed_url == hashed_url).all()
        return True if result else False

    def persist(self, url):
        """
        Persist this URL in the database
        Args:
            url: the url to be persisted
        """
        hashed_url = hash(url)
        tableUrl = TableURL(\
            hashed_url=hashed_url,
            url=url,
            added=date.today()
        )
        self._session.add(tableUrl)
