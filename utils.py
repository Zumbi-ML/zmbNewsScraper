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

# Hash
# ==============================================================================

def hash_url(url):
    """
    Hash a URL with a seed defined in config
    """
    _ensure_pythonhashseed()
    return hash(url)

def _ensure_pythonhashseed(seed=0):
    """
    Ensures that a specific URL returns the same hash everytime
    """
    current_seed = os.environ.get("PYTHONHASHSEED")

    seed = str(seed)
    if current_seed is None or current_seed != seed:
        os.environ["PYTHONHASHSEED"] = seed
        # restart the current process
        os.execl(sys.executable, sys.executable, *sys.argv)

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
