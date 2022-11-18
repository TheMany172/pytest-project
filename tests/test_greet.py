from lib.greet import *

def test_greet_adam():
    result = greet('adam')
    assert result == 'Hello, adam!'
