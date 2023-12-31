import pytest
from services.article_service import ArticleService
from services.source_service import SourceService
from sqlalchemy.exc import SQLAlchemyError

@pytest.fixture
def source_fixture(session):
    source_service = SourceService(session)
    source_map = {'name': "Folha de S. Paulo", 'url_key': 'folha.uol', 'home_url': 'http://folha.uol.com.br', 'enabled': True}
    try:
        source_service.persist(source_map)
        source = source_service.find_source_by_home_url(source_map['home_url'])
        yield source
        source_service.delete_by_id(source.id)
    except SQLAlchemyError:
        session.rollback()
        raise

@pytest.fixture
def article_map():
    return {
        "id": 1,  # ID único para o artigo
        "source_id": 1,  # ID da fonte
        "hashed_url": "hash_example",  # Hash único para a URL do artigo
        "url": "https://example.com/article",  # URL do artigo
        "content": "Este é o conteúdo do artigo.",  # Conteúdo do artigo
        "published_time": "2023-01-01",  # Data de publicação
        "title": "Título do Artigo",  # Título do artigo
        "keywords": "keyword1, keyword2",  # Palavras-chave
        "section": "Notícias",  # Seção do artigo
        "site_name": "Example News",  # Nome do site
        "authors": "Autor1, Autor2",  # Autores do artigo
        "entities": "Entidade1, Entidade2",  # Entidades mencionadas no artigo
        "html": "<html>Conteúdo HTML do artigo</html>",  # Conteúdo HTML do artigo
        "added": "2023-01-02",  # Data de adição do artigo ao banco de dados
        "sent": True,  # Indica se o artigo foi enviado
        "n_sents": 5,  # Número de sentenças no artigo
        "meta_data": "Meta-dados do artigo"  # Meta-dados associados ao artigo
    }

@pytest.fixture
def article_service():
    with ArticleService() as svc:
        yield svc

@pytest.fixture
def setup_and_teardown_article(article_service, article_map):
    # Limpa dados antigos se existirem
    existing_article = article_service.find_article_by_url(article_map['url'])
    if existing_article:
        article_service.delete_article(existing_article.id)

    yield

    # Limpeza após o teste
    created_article = article_service.find_article_by_url(article_map['url'])
    if created_article:
        article_service.delete_article(created_article.id)

"""
def test_persist_article(article_service, article_map, setup_and_teardown_article):
    # Teste o método persist
    article_service.persist(article_map)

    # Verifique se o artigo foi persistido corretamente
    persisted_article = article_service.find_article_by_url(article_map['url'])
    assert persisted_article is not None
"""