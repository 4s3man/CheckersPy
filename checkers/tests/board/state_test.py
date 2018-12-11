import pytest
from checkers.tests.fixtures import *
from checkers.board.state import *

def test_get_win_state(two_queens_state, different_pawns_around_white_state, black_win_state, white_win_state):
    different_pawns_around_white_state.check_for_win()
    assert 'pending' == different_pawns_around_white_state.game_state

    black_win_state.check_for_win()
    assert 'black_win' == black_win_state.game_state

    white_win_state.check_for_win()
    assert 'white_win' == white_win_state.game_state
