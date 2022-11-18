from lib.counter import *

def test_counter_Counter():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_adds_single_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

# we have now tested all the methods, but not all behaviours

def test_multiple_numbers_added():
    counter = Counter()
    counter.add(5)
    counter.add(6)
    assert counter.report() == 'Counted to 11 so far.'

def test_multiple_numbers_added_with_minus():
    counter = Counter()
    counter.add(5)
    counter.add(-6)
    assert counter.report() == 'Counted to -1 so far.'

