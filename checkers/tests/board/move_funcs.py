import pytest
from checkers.board.move_funcs import *

def test_has_only_queens(only_queens_state, for_queen_blocking_pawns_state):
    assert False == has_only_queens(for_queen_blocking_pawns_state)
    assert True == has_only_queens(only_queens_state)
