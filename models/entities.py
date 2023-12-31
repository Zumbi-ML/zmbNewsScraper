from sqlalchemy import Column, Integer, String, Date, Text, Boolean
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from models.max_columns_sizes import *

Base = declarative_base()

class URLEntity(Base):
    # Define a table for storing URL data
    __tablename__ = "tb_urls"
    
    # Ensure hashed_url is unique across the table
    __table_args__ = (UniqueConstraint('hashed_url', name="urlx_2"),)

    # Primary key for the URL entity
    id = Column('id', Integer, primary_key=True)

    # Hashed version of the URL for efficient lookup and comparison
    hashed_url = Column('hashed_url', String(HASH_SIZE), nullable=False)

    # Full URL text, limited by a predefined max size
    url = Column('url', Text(MAX_URL), nullable=False)

    # Date when the URL was added to the database
    added = Column('added', Date, nullable=False)

class ArticleEntity(Base):
    # Define a table for storing articles
    __tablename__ = "tb_articles"

    # Unique constraint on hashed_url and additional table arguments for MySQL specific settings
    __table_args__ = (UniqueConstraint('hashed_url', name="urlx_1"),
                        {'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'})

    # Primary key for the article entity
    id = Column('id', Integer, primary_key=True)

    # Foreign key linking to the source of the article
    source_id = Column('source_id', Integer, ForeignKey('tb_sources.id'), nullable=False)

    # Columns for various attributes of an article
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

    # Establishing a relationship with the SourceEntity
    source = relationship('SourceEntity', back_populates="articles")

class SourceEntity(Base):
    # Define a table for storing information about sources of articles
    __tablename__ = "tb_sources"

    # Unique constraint on url_key for identifying a source
    __table_args__ = (UniqueConstraint('url_key', name="keyulx_1"),)
    
    # Primary key for the source entity
    id = Column('id', Integer, primary_key=True)

    # Columns for various attributes of a source
    name = Column('name', String(MAX_ENTITY_NAME_FIELD))
    # URL key: A subdomain.domain that is used as a key to identifying a source
    url_key = Column('url_key', String(100), nullable=False)
    home_url = Column('home_url', String(MAX_URL))
    enabled = Column('enabled', Boolean, nullable=False)

    # Establishing a relationship with the ArticleEntity
    articles = relationship('ArticleEntity', back_populates="source")
