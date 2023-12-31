import pytest
from models.credentials import get_engine
from utils.utils import get_property
from sqlalchemy.orm import sessionmaker
from services.source_service import SourceService
from services.article_service import ArticleService


@pytest.fixture(scope="module")
def session():
    """
    A session of a DB
    """
    DB_USER = get_property("db_user")
    DB_PWD = get_property("db_pwd")
    DB_HOST = get_property("db_host")
    DB_NAME = get_property("db_name") + "_test"
    DB_DEBUG_MODE = get_property("db_debug_mode") == "True"

    engine = get_engine(db_user=DB_USER, db_pwd=DB_PWD, db_host=DB_HOST, db_name=DB_NAME, db_debug_mode=DB_DEBUG_MODE)
    Session = sessionmaker(bind=engine, autoflush=False)
    return Session()