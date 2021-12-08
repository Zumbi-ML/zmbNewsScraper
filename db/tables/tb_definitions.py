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
    hashed_url = Column('hashed_url', BigInteger, nullable=False)
    url = Column('url', Text(2048), nullable=False)
    added = Column('added', Date, nullable=False)

class TableArticles(Base):
    __tablename__ = "tb_articles"
    __table_args__ = (UniqueConstraint('hashed_url', name="urlx_1"),)
    id = Column('id', Integer, primary_key=True)
    source_id = Column('source_id', Integer, ForeignKey('tb_sources.id'), nullable=False)
    hashed_url = Column('hashed_url', BigInteger, nullable=False)
    url = Column('url', Text(MAX_URL), nullable=False)
    content = Column('content', Text(MAX_CONTENT), nullable=False)
    published_time = Column('published_time', Date)
    title = Column('title', Text(MAX_TITLE))
    keywords = Column('keywords', String(MAX_KEYWORDS))
    section = Column('section', String(MAX_SECTION))
    site_name = Column('site_name', String(MAX_SITE_NAME))
    authors = Column('authors', String(MAX_AUTHORS))
    added = Column('added', Date)
    sent = Column('sent', Boolean, nullable=False)
    table_sources = relationship('TableSources')

class TableSources(Base):
    __tablename__ = "tb_sources"
    __table_args__ = (UniqueConstraint('home_url', name="hrulx_1"),)
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(100))
    home_url = Column('home_url', String(50), nullable=False)
    enabled = Column('enabled', Boolean)
