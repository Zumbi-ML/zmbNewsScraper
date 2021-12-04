# -*- coding: UTF-8 -*-

from .base_service import BaseService
from db.tables.tb_definitions import *
from datetime import date

class ArticleService(BaseService):
    """
    Is in charge of managing the database session for larger tasks
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def persist(self, article_map):
        """
        Persists an article in the database
        Args:
            article_map: a dictionary with the data for persisting articles
        """
        hashed_uri = hash(article_map['uri'])

        article = TableArticles( \
            uri=article_map['uri'],
            hashed_uri=hashed_uri,
            content=article_map['content'],
            published_time=article_map['published_time'],
            source_id=article_map['source_id'],
            title=article_map['title'],
            keywords=article_map['keywords'],
            section=article_map['section'],
            site_name=article_map['site_name'],
            added=date.today(),
        )
        self._session.add(article)

    def persist_all(self, article_map_lst):
        """
        Persists all articles using the same session instance
        Args:
            article_map_lst: a list of article_maps
        """
        for article_map in article_map_lst:
            self.persist(article_map)

    def is_url_in_db(self, a_url):
        """
        Checks whether a given URL is in the DB as a news article
        Args:
            a_url: a news article URL
        """
        hashed_uri = hash(a_url)
        result = self._session.query(TableArticles) \
                           .filter(TableArticles.hashed_uri == hashed_uri).all()
        return True if result else False
