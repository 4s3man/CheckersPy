import pytest
from checkers.tests.fixtures import *
from checkers.board.state import *

def test_get_win_state(two_queens_state, different_pawns_around_white_state, black_win_state, white_win_state):
    assert '' == different_pawns_around_white_state.get_winner()
    assert 'white' == white_win_state.get_winner()
    assert 'black' == black_win_state.get_winner()

def collection_has_moves(no_moves_for_black):
    checkers = Checkers(no_moves_for_black)
    checkers.resolve_moves('black')
    assert False == checkers.state.collection_has_moves('black')

    checkers.resolve_moves('white')
    assert True == checkers.state.collection_has_moves('white')
