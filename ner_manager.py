from config import nlp
from db.tables.max_columns_sizes import *
from config import scrapper_logger
from utils import hash_url

def extract_ents_from_a_sentence(sentence):
    """
    Returns the entities of a sentence
    """
    entities_map = {}

    doc = nlp(sentence)
    for entity in doc.ents:
        if (not entity.label_ in entities_map.keys()):
            entities_map[entity.label_] = set()
        entities_map[entity.label_].add(entity.text)
    return entities_map

def extract_ents_from_an_article(text):
    """
    Returns the entities of an article's text
    Args:
        text: the text of the article
    """
    entities_map = {}

    for sentence in text.split("\n\n"):
        sent_ents_map = extract_ents_from_a_sentence(sentence)
        for label in sent_ents_map.keys():
            if (not label in entities_map.keys()):
                entities_map[label] = sent_ents_map[label]
            entities_map[label].update(sent_ents_map[label])
    return entities_map

def wrap_entities(article_map, logger=scrapper_logger):
    """
    Adds the entities to the article map, respecting the max column size
    """
    entity_map = extract_ents_from_an_article(article_map['content'])
    stringfied = stringfy_ents(entity_map)
    if (len(stringfied) > MAX_ENTITIES):
        url = article_map['url']
        hashed_url = hash_url(url)
        logger.warn(f"Truncated entities:\t{hashed_url}\t{url}")
        stringfied = stringfied[0:MAX_ENTITIES]
    article_map['entities'] = stringfied
    return article_map

# Helper functions
# ==============================================================================

def stringfy_ents(entities_map):
    """
    Converts an entities_map into a string
    """
    stringfied = ""
    for label in entities_map.keys():
        stringfied += label + ":"
        k = 1
        for entity in entities_map[label]:
            stringfied += entity
            if (k < len(entities_map[label])):
                stringfied += ","
            k += 1
        stringfied += ";"
    return stringfied
