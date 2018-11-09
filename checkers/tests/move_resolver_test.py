import pytest
from checkers.board.move_resolver import *

def test_get_pawn_in_direction(different_pawns_around_white_state):
    state = different_pawns_around_white_state
    pawn = state.white_pawns[1]
    border_pawn = state.black_pawns[3]
    move_res = MoveResolver(state)

    assert state.black_pawns[0] is move_res.get_pawn_in_direction(pawn, (-1, -1))
    assert state.black_pawns[0] is not move_res.get_pawn_in_direction(pawn, (-1, 1))

    assert state.white_pawns[2] is move_res.get_pawn_in_direction(pawn, (-1, 1))
    assert state.white_pawns[1] is not move_res.get_pawn_in_direction(pawn, (-1, 1))

    with pytest.raises(NoCoinError):
        assert move_res.get_pawn_in_direction(pawn, (1, 1))

    with pytest.raises(OutOfBoardError):
        assert move_res.get_pawn_in_direction(border_pawn, (-1, 1))

def test_pawn_has_obligtory_move(different_pawns_around_white_state):
    state = different_pawns_around_white_state
    move_res = MoveResolver(state)

    assert True == move_res.pawn_has_obligatory_move(state.white_pawns[1])
    assert False == move_res.pawn_has_obligatory_move(state.white_pawns[2])

    assert True == move_res.pawn_has_obligatory_move(state.black_pawns[0])
    assert False == move_res.pawn_has_obligatory_move(state.black_pawns[1])
    assert False == move_res.pawn_has_obligatory_move(state.black_pawns[2])
    assert False == move_res.pawn_has_obligatory_move(state.black_pawns[3])

def test_pawn_has_obligtory_move_after_move(extended_circle_state):
    state = extended_circle_state
    move_res = MoveResolver(state)
    move = {'pos': [(3, 5)], 'beated_pawn_ids': [2]}
    pawn = copy.deepcopy(state.white_pawns[1])
    pawn.y = 3
    pawn.x = 5

    assert True == move_res.pawn_has_obligatory_move(state.white_pawns[1], move)

def test_get_jump_moves_for_pawn_extended_circle_state(extended_circle_state):
    state = extended_circle_state
    move_res = MoveResolver(state)

    assert [{'positon_after_move': (5, 3), 'beated_pawn_ids': [1, 0, 3, 2]}]\
            == move_res.get_jump_moves_for_pawn(state.white_pawns[1], [])
    assert [
        {'positon_after_move': (7, 7), 'beated_pawn_ids': [3, 2, 4]},
        {'positon_after_move': (5, 1), 'beated_pawn_ids': [3, 1]}
    ] == move_res.get_jump_moves_for_pawn(state.white_pawns[2], [])
