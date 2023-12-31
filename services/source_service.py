# -*- coding: UTF-8 -*-

from services.base_service import BaseService
from models.entities import *

class SourceService(BaseService):
    """
    Is in charge of managing the database session for larger tasks
    """

    def __init__(self, session=None, commit_on_exit=True, close_on_exit=True):
        """
        Constructor
        """
        super().__init__(session=session, commit_on_exit=commit_on_exit, close_on_exit=close_on_exit)

    def find_all_enabled(self):
        """
        Finds all enabled news sources
        """
        results = self._session.query(SourceEntity) \
                                        .filter(SourceEntity.enabled == 1).all()

        home_urls = []
        for row in results:
            home_urls.append({"id": row.id, "home_url": row.home_url})
        return home_urls

    def persist(self, source_map):
        """
        Adds a source_map into the session
        Args:
            source_map: a map mirroring the table sources.
            E.g.:
                {'name': Folha de S. Paulo',
                 'url': 'http://folha.uol.com.br',
                 'enabled': True,}
        """
        source = SourceEntity( \
            name=source_map['name'],
            url_key=source_map['url_key'],
            home_url=source_map['home_url'],
            enabled=source_map['enabled'],
        )
        self._session.add(source)

    def persist_all(self, source_map_lst):
        """
        Adds a list of source_maps into the session
        Args:
            source_map_lst: a list of source_maps.
                            See the method persist for an example of source_map.
        """
        for source_map in source_map_lst:
            self.persist(source_map)

    def find_name_by_id(self, id):
        """
        Returns the name of the source by looking the id
        """
        a_source = self._session.query(SourceEntity) \
                                          .filter(SourceEntity.id == id).first()
        return a_source.name if a_source else None


    def find_source_by_home_url(self, home_url):
        """
        Returns a source dictionary by matching a URL
        """
        entity = self._session.query(SourceEntity) \
                                          .filter(SourceEntity.home_url == home_url).first()

        if (not entity):
            return None
                
        return {
            "id": entity.id,
            "name": entity.name,
            "url_key": entity.url_key,
            "home_url": entity.home_url,
            "enabled": entity.enabled
        }

    def find_source_id_by_url_key(self, url_key):
        """
        Returns the source_id by providing a URL key
        """
        a_source = self._session.query(SourceEntity) \
                                .filter(SourceEntity.url_key == url_key).first()
        return a_source.id if a_source else None
    
    def delete_by_id(self, id):
        """
        Deletes a news source based on its ID
        Args:
            id: The ID of the source to be deleted.
        """
        source_to_delete = self._session.query(SourceEntity) \
                                        .filter(SourceEntity.id == id).first()
        if source_to_delete:
            self._session.delete(source_to_delete)
        else:
            raise ValueError("Source with ID {} not found".format(id))
        
    def update(self, id, source_map):
        """
        Updates a news source based on the provided map
        Args:
            id: The ID of the source to be updated.
            source_map: A map containing the fields to be updated.
                        Fields not provided in the map will remain unchanged.
        """
        source_to_update = self._session.query(SourceEntity) \
                                        .filter(SourceEntity.id == id).first()
        if source_to_update:
            for key, value in source_map.items():
                if hasattr(source_to_update, key):
                    setattr(source_to_update, key, value)
                else:
                    raise AttributeError("Attribute {} not found in SourceEntity".format(key))
        else:
            raise ValueError("Source with ID {} not found".format(id))


