# -*- coding: UTF-8 -*-

from ..db.base_service import BaseService
from db.tables.tb_definitions import *
from datetime import date
from utils.hasher import hash_url

class UrlService(BaseService):

    def __init__(self, session=None, commit_on_exit=True, close_on_exit=True):
        """
        Constructor
        """
        super().__init__(session=session, commit_on_exit=commit_on_exit, close_on_exit=close_on_exit)

    def has_url_been_seen(self, a_url):
        """
        Checks whether a given URL
        Args:
            a_url: a news article URL
        """
        hashed_url = hash_url(a_url)
        result = self._session.query(TableURL) \
                           .filter(TableURL.hashed_url == hashed_url).all()
        return True if result else False

    def persist(self, url):
        """
        Persist this URL in the database
        Args:
            url: the url to be persisted
        """
        hashed_url = hash_url(url)
        tableUrl = TableURL(\
            hashed_url=hashed_url,
            url=url,
            added=date.today()
        )
        self._session.add(tableUrl)
