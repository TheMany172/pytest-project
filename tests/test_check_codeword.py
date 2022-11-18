from lib.check_codeword import *

def test_codeword_correct_horse():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_codeword_close_h_e():
    result = check_codeword('house')
    assert result == 'Close, but nope.'

def test_codeword_wrong_other_word():
    result = check_codeword('penguin')
    assert result == 'WRONG!'
