from datetime import date
from e_map import ents_2_api_map
import os
import sys

def get_property(property):
    """
    Return a property in the properties file
    Args:
        property: name of the property. E.g. db_user
    """
    with open(".properties") as f:
        line = f.readline()
        while (line):
            if (property in line):
                p = line.split(":")[1]
                return p.strip()
            line = f.readline()
    return None

def str2date(str_date, sep="-"):
    year, month, day = str_date.split(sep)
    return date(int(year), int(month), int(day))

def convert_into_api_format(entities_map):
    """
    """
    api_entities_map = {}
    for entity_label in entities_map.keys():
        api_label = ents_2_api_map[entity_label]
        if (not api_label in api_entities_map.keys()):
            api_entities_map[api_label] = []
        for entity in entities_map[entity_label]:
            api_entities_map[api_label].append(entity)
    return api_entities_map
