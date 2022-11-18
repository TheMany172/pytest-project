import pytest
from lib.password_checker import *

def test_check_length():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check('AdamLittle') == True

def test_check_length_error():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as error:
        passwordchecker.check('Adam')
    error_message = str(error.value)
    assert error_message == "Invalid password, must be 8+ characters."