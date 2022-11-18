from lib.gratitudes import *


def test_gratitudes_empty():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []


def test_add_to_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add('being awesome')
    gratitudes.add('being a ninja')
    assert gratitudes.gratitudes == ['being awesome', 'being a ninja']

def test_format_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add('being awesome')
    gratitudes.add('being relentless')
    assert gratitudes.format() == 'Be grateful for: being awesome, being relentless'