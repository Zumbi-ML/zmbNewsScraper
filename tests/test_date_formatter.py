# -*- coding: UTF-8 -*-

from date_formatter import date_format

def test_format_date1():
    a_date = "Mon, 07 Dec 2020 20:22:19 GM"
    assert date_format(a_date) == "2020-12-07"

def test_format_date2():
    a_date = "2020-11-23-0306:00:00-10800"
    assert date_format(a_date) == "2020-11-23"

def test_format_date3():
    a_date = "2011-11-04T00:05:23"
    assert date_format(a_date) == "2011-11-04"

def test_format_date4():
    a_date = "2011-11-04T00:05:23+04:00"
    assert date_format(a_date) == "2011-11-04"

def test_format_date5():
    a_date = "2011-11-04 00:05:23.283"
    assert date_format(a_date) == "2011-11-04"

def test_format_date6():
    a_date = "2011-11-04 00:05:23.283+00:00"
    assert date_format(a_date) == "2011-11-04"

def test_format_date7():
    a_date = "2011-11-04"
    assert date_format(a_date) == "2011-11-04"

def test_format_date8():
    a_date = "04/11/2011"
    assert date_format(a_date) == "2011-11-04"

def test_format_date9():
    a_date = "04/11/11"
    assert date_format(a_date) == None

def test_format_date10():
    a_date = "04 11 2011"
    assert date_format(a_date) == "2011-11-04"

def test_format_date11():
    a_date = "2021-03-16T9:35"
    assert date_format(a_date) == "2021-03-16"
