import pytest
from services.source_service import SourceService

@pytest.fixture
def source_map():
    return {'name': "Folha de S. Paulo", 'url_key': 'folha.uol', 'home_url': 'http://folha.uol.com.br', 'enabled': True}

@pytest.fixture
def source_service():
    with SourceService() as srv:
        yield srv

@pytest.fixture
def setup_and_teardown_source(source_service, source_map):
    # Limpa dados antigos se existirem
    existing_source = source_service.find_source_by_home_url(source_map['home_url'])
    if existing_source:
        source_service.delete_by_id(existing_source['id'])

    yield

    # Limpeza após o teste
    created_source = source_service.find_source_by_home_url(source_map['home_url'])
    if created_source:
        source_service.delete_by_id(created_source['id'])

def test_persist_source(source_map, source_service):
    # Persist the source
    source_service.persist(source_map)
    # Retrieve the source to verify persistence
    retrieved = source_service.find_source_by_home_url(source_map['home_url'])
    assert retrieved is not None

def test_find_source_by_home_url(source_map, source_service):
    # Assume the source is already persisted
    retrieved = source_service.find_source_by_home_url(source_map['home_url'])
    assert retrieved['home_url'] == source_map['home_url']

def test_update_source(source_map, source_service):
    # Assume the source is already persisted
    new_data = {'name': "Updated Name"}
    source_id = source_service.find_source_id_by_url_key(source_map['url_key'])
    source_service.update(source_id, new_data)
    # Retrieve updated source
    updated_source = source_service.find_source_by_home_url(source_map['home_url'])
    assert updated_source['name'] == new_data['name']

def test_delete_source(source_map, source_service):
    # Assume the source is already persisted
    source_id = source_service.find_source_id_by_url_key(source_map['url_key'])
    source_service.delete_by_id(source_id)
    # Try to retrieve deleted source
    deleted_source = source_service.find_source_by_home_url(source_map['home_url'])
    assert deleted_source is None
