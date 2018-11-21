import pytest
from checkers.checkers import *

def test_make_move(initial_state):
    checkers = Checkers(initial_state)
    assert True == checkers.make_move({'dono'})
