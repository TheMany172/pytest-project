from lib.report_length import *

def test_length_is_length_of_string():
    result = report_length('mildred')
    assert result == 'This string was 7 characters long.'