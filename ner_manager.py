from db.tables.max_columns_sizes import *
from config import scrapper_logger
import json
from hasher import hash_url
from zmbner.spacy import ZmbNER

def wrap_entities(article_map, logger=scrapper_logger):
    """
    Adds the entities to the article map, respecting the max column size
    """
    entity_map = ZmbNER.ents(article_map['content'])
    print(entity_map)
    stringfied = json.dumps(entity_map)
    if (len(stringfied) > MAX_ENTITIES):
        url = article_map['url']
        hashed_url = hash_url(url)
        logger.warn(f"Truncated entities:\t{hashed_url}\t{url}")
        stringfied = '{"message": "truncated"}'
    article_map['entities'] = stringfied
    return article_map
