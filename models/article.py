# -*- coding: UTF-8 -*-

from services.base_service import BaseDAO
from models.entities import ArticleEntity
from datetime import date
from utils.hasher import hash_url

# DAO
# ====================================================================================================================================================================
class ArticleDAO(BaseDAO):
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
        #article_map['source_id'] = article.source_id
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
        return self.convert_db_article_into_map(article)

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
        


# Model
# ====================================================================================================================================================================
        
class Article:
    def __init__(self):
        self._hashed_url = None
        self._url = None
        self._content = None
        self._published_time = None
        self._title = None
        self._keywords = None
        self._section = None
        self._site_name = None
        self._authors = None
        self._entities = None
        self._html = None
        self._meta_data = None
        self._added = None
        self._sent = None
        self._n_sents = None

    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value

    @property
    def hashed_url(self):
        return self._hashed_url

    @hashed_url.setter
    def hashed_url(self, value):
        self._hashed_url = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def published_time(self):
        return self._published_time

    @published_time.setter
    def published_time(self, value):
        self._published_time = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        self._keywords = value

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        self._section = value

    @property
    def site_name(self):
        return self._site_name

    @site_name.setter
    def site_name(self, value):
        self._site_name = value

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, value):
        self._authors = value

    @property
    def entities(self):
        return self._entities

    @entities.setter
    def entities(self, value):
        self._entities = value

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value

    @property
    def meta_data(self):
        return self._meta_data

    @meta_data.setter
    def meta_data(self, value):
        self._meta_data = value

    @property
    def added(self):
        return self._added

    @added.setter
    def added(self, value):
        self._added = value

    @property
    def sent(self):
        return self._sent

    @sent.setter
    def sent(self, value):
        self._sent = value

    @property
    def n_sents(self):
        return self._n_sents

    @n_sents.setter
    def n_sents(self, value):
        self._n_sents = value
