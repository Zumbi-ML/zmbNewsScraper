# -*- coding: UTF-8 -*-

import re

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
DAYS_OF_WEEK = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

def date_format(a_date):
    """
    Converts a_date to proper format
    Args:
        a_date: the date as a string to be converted
    """
    a_date = re.sub(r"T.*", "", a_date)
    a_date = re.sub(r"[ -](\d{2})?\d\d:\d\d.*", "", a_date)
    a_date = re.sub(r",", "", a_date)

    if (date_contains_spelled_dow(a_date)):
        a_date = remove_dow(a_date)

    if (date_contains_spelled_month(a_date)):
        a_date = sub_spelled_month(a_date)

    a_date = a_date.strip()
    sep = get_separator(a_date)
    year, month, day = split_into_year_mon_day(a_date, sep)

    if (all([year, month, day])):
        return f"{year}-{month}-{day}"

    return None

def get_separator(a_date):
    """
    Determines the separator for a string date
    Args:
        a_date: A string date "2011-12-31"
    """
    sep = None
    if (" " in a_date):
        sep = " "
    elif ("-" in a_date):
        sep = "-"
    elif ("/" in a_date):
        sep = "/"
    return sep

def split_into_year_mon_day(a_date, sep):
    """
    Breaks the date into year month and day.
    Args:
        a_date: a string date to be separated
        sep: the separator
    """

    year, month, day = None, None, None
    parts = a_date.split(sep)

    if (len(parts) != 3):
        return None, None, None

    if is_a_year(parts[0]):
        year = pad_with_zero(parts[0])
        day_idx = 2
    elif is_a_year(parts[2]):
        year = pad_with_zero(parts[2])
        day_idx = 0
    else:
        # If the year cannot be determined, return None
        return None, None, None

    day = None
    if is_a_day_of_month(parts[day_idx]):
        day = pad_with_zero(parts[day_idx])
    else:
        return None, None, None

    month = None
    if is_a_month(parts[1]):
        month = pad_with_zero(parts[1])
    else:
        return None, None, None

    return year, month, day

def pad_with_zero(date_part):
    """
    Pads a date part with zero if necessary
    """
    int_dp = int(date_part)
    padded = "0" + str(int_dp) if int_dp < 10 else str(int_dp)
    return padded

def is_a_year(date_part):
    """
    Determines if a date part can be considered a year
    Args:
        date_part: Ex: "2011"
    """
    if (int(date_part) > 1970):
        return True
    return False

def is_a_month(date_part):
    """
    Determines if a date part can be considered a month
    Args:
        date_part:  Ex: "12"
    """
    if (int(date_part) >= 1 and int(date_part) <= 12):
        return True
    return False

def is_a_day_of_month(date_part):
    """
    Determines if a date_part can be considered a day of month
    Args:
        date_part: Ex: "31"
    """
    if (int(date_part) >= 1 and int(date_part) <= 31):
        return True
    return False

def date_contains_spelled_month(a_date):
    """
    Checks if a_date contains spelled month
    Args:
        a_date: Ex: "Mon, 07 Dec 2020"
    """
    for month in MONTHS:
        if (month in a_date.lower()):
            return True
    return False

def sub_spelled_month(a_date):
    """
    Substitutes the spelled month for its numeric version
    Args:
        a_date: Ex: "Mon, 07 Dec 2020" => "Mon, 07 12 2020"
    """
    for month in MONTHS:
        if (month in a_date.lower()):
            num_month = MONTHS.index(month) + 1
            str_month = pad_with_zero(num_month)
            return re.sub(month, str_month, a_date.lower())

def date_contains_spelled_dow(a_date):
    """
    Checks if a_date contains spelled month
    Args:
        a_date: Ex: "Mon, 07 Dec 2020"
    """
    for dow in DAYS_OF_WEEK:
        if (dow in a_date.lower()):
            return True
    return False

def remove_dow(a_date):
    """
    Removes days of week
    Args:
        a_date: Ex: "Mon, 07 Dec 2020" => ", 07 12 2020"
    """
    nd = None
    for dow in DAYS_OF_WEEK:
        if (dow in a_date.lower()):
            nd = re.sub(dow, "", a_date.lower())
    return nd
