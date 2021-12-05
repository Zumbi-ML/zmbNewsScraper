from datetime import date
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

def hash_url(url):
    """
    Hash a URL with a seed defined in config
    """
    _ensure_pythonhashseed()
    return hash(url)

# Hash
# ==============================================================================

def _ensure_pythonhashseed(seed=0):
    current_seed = os.environ.get("PYTHONHASHSEED")

    seed = str(seed)
    if current_seed is None or current_seed != seed:
        os.environ["PYTHONHASHSEED"] = seed
        # restart the current process
        os.execl(sys.executable, sys.executable, *sys.argv)
