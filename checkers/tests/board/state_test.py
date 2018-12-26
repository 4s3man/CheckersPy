import pytest
from checkers.tests.fixtures import *
from checkers.board.state import *

# TODO: add state make move

def test_has_only_queens(only_queens_state, for_queen_blocking_pawns_state):
    assert False == for_queen_blocking_pawns_state.has_only_queens()
    assert True == only_queens_state.has_only_queens()


def test_get_pawn_collection(no_blocked_beating_move_bug):
    assert no_blocked_beating_move_bug.white_pawns == no_blocked_beating_move_bug.get_pawn_collection(Color('white'))
    assert no_blocked_beating_move_bug.black_pawns == no_blocked_beating_move_bug.get_pawn_collection(Color('black'))

    with pytest.raises(ValueError):
        assert no_blocked_beating_move_bug.get_pawn_collection(Color('bad_color'))

def test_json_convert(no_blocked_beating_move_bug):
    json_state = State().json_encode()
    state_from_json = State(json_state)

    assert True == (state_from_json == State())
    assert False == (no_blocked_beating_move_bug == State())

def collection_has_moves(no_moves_for_black):
    checkers = Checkers(no_moves_for_black)
    checkers.resolve_moves(Color('black'))
    assert False == checkers.state.collection_has_moves(Color('black'))

    checkers.resolve_moves('white')
    assert True == checkers.state.collection_has_moves(Color('white'))

def test_get_winner(two_queens_state, different_pawns_around_white_state, black_win_state, white_win_state):
    assert '' == different_pawns_around_white_state.get_winner()
    assert 'white' == white_win_state.get_winner()
    assert 'black' == black_win_state.get_winner()
