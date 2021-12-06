from sqlalchemy import Column, Integer, BigInteger, String, Date, Text, Boolean
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    url = Column('url', Text(2048), nullable=False)
    content = Column('content', Text(30000), nullable=False)
    published_time = Column('published_time', Date)
    title = Column('title', Text(200))
    keywords = Column('keywords', String(400))
    section = Column('section', String(50))
    site_name = Column('site_name', String(50))
    authors = Column('authors', String(100))
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
