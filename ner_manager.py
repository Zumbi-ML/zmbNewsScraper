from config import nlp
import article_manager

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

#article = article_manager.find_article_by_id(1)
#print(extract_ents_from_an_article(article['content']))
