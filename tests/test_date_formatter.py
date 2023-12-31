# -*- coding: UTF-8 -*-
import pytest
from utils.date_formatter import date_format

# The 'parametrize' decorator is used to test the 'date_format' function with multiple sets of inputs and expected outputs.
# This approach allows for comprehensive testing of different date formats and scenarios in a concise manner.
@pytest.mark.parametrize("test_input,expected", [
    ("Mon, 07 Dec 2020 20:22:19 GM", "2020-12-07"),     # Test with full date string including day and time zone.
    ("2020-11-23-0306:00:00-10800", "2020-11-23"),     # Test with date string containing time and offset.
    ("2011-11-04T00:05:23", "2011-11-04"),             # Test ISO 8601 format with time.
    ("2011-11-04T00:05:23+04:00", "2011-11-04"),       # Test ISO 8601 format with time zone offset.
    ("2011-11-04 00:05:23.283", "2011-11-04"),         # Test with milliseconds.
    ("2011-11-04 00:05:23.283+00:00", "2011-11-04"),   # Test with milliseconds and time zone offset.
    ("2011-11-04", "2011-11-04"),                      # Test with simple YYYY-MM-DD format.
    ("04/11/2011", "2011-11-04"),                      # Test with DD/MM/YYYY format.
    ("04/11/11", None),                                # Test with ambiguous DD/MM/YY format (expected to fail).
    ("04 11 2011", "2011-11-04"),                      # Test with space-separated date.
    ("2021-03-16T9:35", "2021-03-16"),                 # Test with ISO 8601 format without seconds.
    ("2020-10-4T9:00", "2020-10-04"),                  # Test with ISO 8601 format and single-digit day.
    ("2020|10|04", None)                               # Test with an unknown separator (expected to fail).
])
def test_format_date(test_input, expected):
    # Each assertion checks if the formatted output matches the expected output.
    assert date_format(test_input) == expected
