# -*- coding: UTF-8 -*-

from services.base_service import BaseService
from models.entities import ArticleEntity
from datetime import date
from utils.hasher import hash_url

class ArticleService(BaseService):
    """
    Is in charge of managing the database session for larger tasks
    """
    def __init__(self, session=None, commit_on_exit=True, close_on_exit=True):
        """
        Constructor
        """
        super().__init__(session=session, commit_on_exit=commit_on_exit, close_on_exit=close_on_exit)

    def persist(self, article_map):
        """
        Persists an article in the database
        Args:
            article_map: a dictionary with the data for persisting articles
        """
        hashed_url = hash_url(article_map['url'])

        article = ArticleEntity( \
            source_id = article_map['source_id'],
            hashed_url = hashed_url,
            url = article_map['url'],
            content = article_map['content'],
            published_time = article_map['published_time'],
            title = article_map['title'],
            keywords = article_map['keywords'],
            section = article_map['section'],
            site_name = article_map['site_name'],
            authors = article_map['authors'],
            entities = article_map['entities'],
            html = article_map['html'],
            meta_data = article_map['meta_data'],
            added = date.today(),
            sent = False,
            n_sents = 0,
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
        hashed_url = hash_url(a_url)
        result = self._session.query(ArticleEntity) \
                           .filter(ArticleEntity.hashed_url == hashed_url).all()
        return True if result else False

    def read_all_articles_not_sent(self):
        """
        Returns all articles not marked as sent
        """
        articles = self._session.query(ArticleEntity) \
                            .filter(ArticleEntity.sent == False).all()

        article_map_lst = []
        for article in articles:
            article_map = self.convert_db_article_into_map(article)
            article_map_lst.append(article_map)
        return article_map_lst

    def convert_db_article_into_map(self, article):
        """
        Converts an article returned from DB into a map
        Args:
            article: ArticleEntity object
        """
        article_map = {}
        article_map['source_id'] = article.source_id
        article_map['hashed_url'] = article.hashed_url
        article_map['url'] = article.url
        article_map['content'] = article.content
        article_map['published_time'] = article.published_time
        article_map['title'] = article.title
        article_map['keywords'] = article.keywords
        article_map['section'] = article.section
        article_map['site_name'] = article.site_name
        article_map['authors'] = article.authors
        article_map['entities'] = article.entities
        article_map['added'] = article.added
        article_map['sent'] = article.sent
        article_map['html'] = article.html
        article_map['meta_data'] = article.meta_data
        return article_map

    def find_article_by_id(self, id):
        """
        Returns an article by providing its database id
        """
        article = self._session.query(ArticleEntity) \
                                         .filter(ArticleEntity.id == id).first()
        if (article):
            return self.convert_db_article_into_map(article)
        return None

    def find_article_by_url(self, url):
        """
        Returns an article by providing its database id
        """
        hashed_url = hash_url(url)
        article = self._session.query(ArticleEntity) \
                                         .filter(ArticleEntity.hashed_url == hashed_url).first()
        if (article):
            return self.convert_db_article_into_map(article)
        return None

    def mark_article_as_sent(self, a_url):
        """
        Marks an article as sent in the database
        Args:
            a_url: the URL to be marked as sent
        """
        hashed_url = hash_url(a_url)
        self._session.query(ArticleEntity) \
                                .filter(ArticleEntity.hashed_url == hashed_url) \
                                    .update({ArticleEntity.sent: True})
        
    def update_article(self, article_id, updated_article_map):
        """
        Updates an article in the database
        Args:
            article_id: the ID of the article to be updated
            updated_article_map: a dictionary with the updated article data
        """
        article = self._session.query(ArticleEntity).filter(ArticleEntity.id == article_id).first()
        if article:
            for key, value in updated_article_map.items():
                setattr(article, key, value)
            self._session.commit()
        else:
            # Handle the case where the article does not exist
            pass

    def delete_article(self, article_id):
        """
        Deletes an article from the database
        Args:
            article_id: the ID of the article to be deleted
        """
        article = self._session.query(ArticleEntity).filter(ArticleEntity.id == article_id).first()
        if article:
            self._session.delete(article)
            self._session.commit()
        else:
            # Handle the case where the article does not exist
            pass


