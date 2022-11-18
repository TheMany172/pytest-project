from lib.string_builder import *

def test_StringBuilder_empty():
    stringbuilder = StringBuilder()
    assert stringbuilder.str == ''

def test_StringBuilder_output_empty():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ''

def test_str_add_str():
    stringbuilder = StringBuilder()
    stringbuilder.add("Adam")
    stringbuilder.add(' Little')
    assert stringbuilder.str == 'Adam Little'

def test_str_add_str_length():
    stringbuilder = StringBuilder()
    stringbuilder.add("Adam")
    stringbuilder.add(' Little')
    assert stringbuilder.size() == 11

def test_str_add_str_output():
    stringbuilder = StringBuilder()
    stringbuilder.add("Adam")
    stringbuilder.add(' Daniel Little')
    assert stringbuilder.output() == 'Adam Daniel Little'
