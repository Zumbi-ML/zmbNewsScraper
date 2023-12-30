from sqlalchemy import Column, Integer, BigInteger, String, Date, Text, Boolean
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .max_columns_sizes import *

Base = declarative_base()

class TableURL(Base):
    __tablename__ = "tb_urls"
    __table_args__ = (UniqueConstraint('hashed_url', name="urlx_2"),)
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), nullable=False)
    url = Column('url', Text(2048), nullable=False)
    added = Column('added', Date, nullable=False)

class TableArticles(Base):
    __tablename__ = "tb_articles"
    __table_args__ = (UniqueConstraint('hashed_url', name="urlx_1"),
                        {'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'})

    id = Column('id', Integer, primary_key=True)
    source_id = Column('source_id', Integer, ForeignKey('tb_sources.id'), nullable=False)
    hashed_url = Column('hashed_url', String(HASH_SIZE), nullable=False)
    url = Column('url', Text(MAX_URL), nullable=False)
    content = Column('content', Text(MAX_CONTENT), nullable=False)
    published_time = Column('published_time', Date)
    title = Column('title', Text(MAX_TITLE))
    keywords = Column('keywords', String(MAX_KEYWORDS))
    section = Column('section', String(MAX_SECTION))
    site_name = Column('site_name', String(MAX_SITE_NAME))
    authors = Column('authors', String(MAX_AUTHORS))
    entities = Column('entities', String(MAX_ENTITIES))
    html = Column('html', Text(MAX_HTML))
    added = Column('added', Date)
    sent = Column('sent', Boolean, nullable=False)
    n_sents = Column('n_sents', Integer)
    meta_data = Column('meta_data', Text(MAX_METADATA))
    table_sources = relationship('TableSources')

class TableSources(Base):
    __tablename__ = "tb_sources"
    __table_args__ = (UniqueConstraint('url_key', name="keyulx_1"),)
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD))
    # URL key: A subdomain.domain that is used as a key to identifying a source
    url_key = Column('url_key', String(100), nullable=False)
    home_url = Column('home_url', String(MAX_URL))
    enabled = Column('enabled', Boolean, nullable=False)
