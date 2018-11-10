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

    assert [{'positon_after_move': (5, 7), 'beated_pawn_ids': [2, 3]}, {'positon_after_move': (1, 5), 'beated_pawn_ids': [1]}]\
    == move_res.get_queen_jump_moves(queen)
    assert [{'positon_after_move': (5, 7), 'beated_pawn_ids': [2]}, {'positon_after_move': (1, 5), 'beated_pawn_ids': [1]}]\
    != move_res.get_queen_jump_moves(queen)

def test_get_queen_jump_moves_for_queen_blocking_pawns_state(for_queen_blocking_pawns_state):
    state = for_queen_blocking_pawns_state
    move_res = MoveResolver(state)
    queen = state.white_pawns[1]

    assert [{'positon_after_move': (5, 7), 'beated_pawn_ids': [2, 3]}, {'positon_after_move': (0, 2), 'beated_pawn_ids': [0, 4]}]\
    == move_res.get_queen_jump_moves(queen)
    assert [{'positon_after_move': (5, 7), 'beated_pawn_ids': []}, {'positon_after_move': (0, 2), 'beated_pawn_ids': [0, 4]}]\
    != move_res.get_queen_jump_moves(queen)
