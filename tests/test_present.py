import pytest
from lib.present import *

def test_present_wrap():
    present = Present()
    present.wrap('bike')
    assert present.contents == 'bike'

def test_present_unwrap():
    present = Present()
    present.wrap('bottle')
    present.unwrap
    assert present.unwrap() == 'bottle'

def test_present_wrap_when_wrapped():
    present = Present()
    present.wrap('bike')
    with pytest.raises(Exception) as err:
        present.wrap(11)
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_present_cannot_unwrap():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."


