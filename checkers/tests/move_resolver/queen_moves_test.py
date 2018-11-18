import pytest
from checkers.board.move_resolver import *

def test_get_pawn_in_line(for_queen_state):
    state = for_queen_state
    move_res = MoveResolver(state)
    queen = state.white_pawns[1]

    assert state.black_pawns[0] == move_res.get_pawn_in_line(queen, (-1,-1))
    assert state.black_pawns[1] == move_res.get_pawn_in_line(queen, (-1,1))
    assert state.black_pawns[2] == move_res.get_pawn_in_line(queen, (1,1))
    assert None == move_res.get_pawn_in_line(queen, (1,-1))

def test_get_queen_jump_moves_for_queen_state(for_queen_state, for_queen_blocking_pawns_state):
    state = for_queen_state
    move_res = MoveResolver(state)
    queen = state.white_pawns[1]

    assert [{'position_after_move': (5, 7), 'beated_pawn_ids': [2, 3]}, {'position_after_move': (1, 5), 'beated_pawn_ids': [1]}]\
    == move_res.get_queen_jump_moves(queen)
    assert [{'position_after_move': (5, 7), 'beated_pawn_ids': [2]}, {'position_after_move': (1, 5), 'beated_pawn_ids': [1]}]\
    != move_res.get_queen_jump_moves(queen)

def test_get_queen_jump_moves_for_queen_blocking_pawns_state(for_queen_blocking_pawns_state):
    state = for_queen_blocking_pawns_state
    move_res = MoveResolver(state)
    queen = state.white_pawns[1]

    assert [{'position_after_move': (5, 7), 'beated_pawn_ids': [2, 3]}, {'position_after_move': (0, 2), 'beated_pawn_ids': [0, 4]}]\
    == move_res.get_queen_jump_moves(queen)
    assert [{'position_after_move': (5, 7), 'beated_pawn_ids': []}, {'position_after_move': (0, 2), 'beated_pawn_ids': [0, 4]}]\
    != move_res.get_queen_jump_moves(queen)

def test_get_queen_normal_moves_normal_moves_state(for_queen_normal_moves_state):
    state = for_queen_normal_moves_state
    move_res = MoveResolver(state)
    queen = state.white_pawns[1]

    assert [{'position_after_move': (5, 3)}, {'position_after_move': (6, 4)}, {'position_after_move': (7, 5)}, {'position_after_move': (5, 1)}, {'position_after_move': (6, 0)}, {'position_after_move': (3, 1)}, {'position_after_move': (2, 0)}, {'position_after_move': (3, 3)}, {'position_after_move': (2, 4)}, {'position_after_move': (1, 5)}, {'position_after_move': (0, 6)}]\
    == move_res.get_queen_normal_moves(queen)
    assert [{'position_after_move': (5, 1)}, {'position_after_move': (6, 4)}, {'position_after_move': (7, 5)}, {'position_after_move': (5, 1)}, {'position_after_move': (6, 0)}, {'position_after_move': (3, 1)}, {'position_after_move': (2, 0)}, {'position_after_move': (3, 3)}, {'position_after_move': (2, 4)}, {'position_after_move': (1, 5)}, {'position_after_move': (0, 6)}]\
    != move_res.get_queen_normal_moves(queen)

def test_get_queen_normal_moves_blocking_pawns_state(for_queen_blocking_pawns_state):
    state = for_queen_blocking_pawns_state
    move_res = MoveResolver(state)
    queen = state.white_pawns[1]

    assert [{'position_after_move': (5, 3)}, {'position_after_move': (5, 1)}, {'position_after_move': (6, 0)}, {'position_after_move': (3, 3)}]\
    == move_res.get_queen_normal_moves(queen)
    assert [{'position_after_move': (5, 1)}, {'position_after_move': (6, 0)}, {'position_after_move': (3, 3)}]\
    != move_res.get_queen_normal_moves(queen)
