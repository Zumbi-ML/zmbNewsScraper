from sqlalchemy import Column, Integer, BigInteger, String, Date, Text, Boolean
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TableArticles(Base):
    __tablename__ = "tb_articles"
    __table_args__ = (UniqueConstraint('hashed_uri', name="urix_1"),)
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, nullable=False)
    uri = Column('uri', Text(2048), nullable=False)
    content = Column('content', Text(30000), nullable=False)
    published_time = Column('published_time', Date)
    source_id = Column('source_id', Integer, ForeignKey('tb_sources.id'), nullable=False)
    title = Column('title', Text(200))
    added = Column('added', Date)
    keywords = Column('keywords', String(400))
    section = Column('section', String(50))
    site_name = Column('site_name', String(50))
    table_sources = relationship('TableSources')

class TableSources(Base):
    __tablename__ = "tb_sources"
    __table_args__ = (UniqueConstraint('home_url', name="hrulx_1"),)
    id = Column('id', Integer, primary_key=True)
    home_url = Column('home_url', String(50), nullable=False)
    enabled = Column('enabled', Boolean)
