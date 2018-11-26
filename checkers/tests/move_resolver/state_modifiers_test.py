import pytest
from checkers.board.move_resolver import *

def test_resolve_moves__initial_state(initial_state):
    state = initial_state
    move_res = MoveResolver(state)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)
    move_res.leave_max_beating_moves_only(state.white_pawns)
    move_res.leave_max_beating_moves_only(state.black_pawns)

    for i in range(4,12):
        assert [] == state.white_pawns[i].moves

    assert [{'position_after_move': (4, 2)}, {'position_after_move': (4, 0)}]\
    == state.white_pawns[0].moves

    assert [{'position_after_move': (4, 4)}, {'position_after_move': (4, 2)}]\
    == state.white_pawns[1].moves

    assert [{'position_after_move': (4, 6)}, {'position_after_move': (4, 4)}]\
    == state.white_pawns[2].moves

    assert [{'position_after_move': (4, 6)}]\
    == state.white_pawns[3].moves

    for i in range(8):
        assert [] == state.black_pawns[i].moves

    assert [{'position_after_move': (3, 1)}]\
    == state.black_pawns[8].moves

    assert [{'position_after_move': (3, 3)}, {'position_after_move': (3, 1)}]\
    == state.black_pawns[9].moves

    assert [{'position_after_move': (3, 5)}, {'position_after_move': (3, 3)}]\
    == state.black_pawns[10].moves

    assert [{'position_after_move': (3, 7)}, {'position_after_move': (3, 5)}]\
    == state.black_pawns[11].moves

def test_resolve_moves__different_pawns_around_white(different_pawns_around_white_state):
    state = different_pawns_around_white_state
    move_res = MoveResolver(state)

    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)
    move_res.leave_max_beating_moves_only(state.white_pawns)
    move_res.leave_max_beating_moves_only(state.black_pawns)

    assert [{'position_after_move': (1, 1), 'beated_pawn_ids': [0]}]\
    ==state.white_pawns[1].moves

    assert []\
    ==state.white_pawns[2].moves

    assert [{'position_after_move': (4, 4), 'beated_pawn_ids': [1]}]\
    ==state.black_pawns[0].moves

    assert []\
    ==state.black_pawns[1].moves

    assert []\
    ==state.black_pawns[2].moves

    assert []\
    ==state.black_pawns[3].moves

def test_resolve_moves_for_all_collections__extended_circle_state(extended_circle_state):
    state = extended_circle_state
    move_res = MoveResolver(state)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)
    move_res.leave_max_beating_moves_only(state.white_pawns)
    move_res.leave_max_beating_moves_only(state.black_pawns)

    assert [{'position_after_move': (5, 3), 'beated_pawn_ids': [1, 0, 3, 2]}] \
    ==state.white_pawns[1].moves

    assert [] \
    ==state.white_pawns[2].moves

    assert [] \
    ==state.white_pawns[3].moves

    assert [] \
    ==state.white_pawns[4].moves

    assert [] \
    ==state.black_pawns[0].moves

    assert [{'position_after_move': (6, 4), 'beated_pawn_ids': [1]}] \
    ==state.black_pawns[1].moves

    assert [{'position_after_move': (6, 2), 'beated_pawn_ids': [1]}] \
    ==state.black_pawns[2].moves

    assert [{'position_after_move': (0, 6), 'beated_pawn_ids': [2]}] \
    ==state.black_pawns[3].moves

    assert [] \
    ==state.black_pawns[4].moves

    assert [] \
    ==state.black_pawns[5].moves

    assert [] \
    ==state.black_pawns[6].moves

def test_resolve_moves__queen_extended_circle_state(queen_extended_circle_state):
    state = queen_extended_circle_state
    move_res = MoveResolver(state)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)
    move_res.leave_max_beating_moves_only(state.white_pawns)
    move_res.leave_max_beating_moves_only(state.black_pawns)

    assert [{'position_after_move': (5, 3), 'beated_pawn_ids': [2, 3, 0, 1]}] \
    ==state.white_pawns[1].moves

    assert [{'position_after_move': (1, 3), 'beated_pawn_ids': [3, 2, 1, 0]}] \
    ==state.white_pawns[2].moves

    assert [{'position_after_move': (1, 3), 'beated_pawn_ids': [0, 1, 2, 3]}] \
    ==state.white_pawns[3].moves

    assert [{'position_after_move': (3, 5), 'beated_pawn_ids': [2, 1, 0, 3]}] \
    ==state.white_pawns[4].moves

    assert [{'position_after_move': (3, 3)}, {'position_after_move': (3, 1)}] \
    ==state.black_pawns[0].moves

    assert [{'position_after_move': (5, 3)}, {'position_after_move': (5, 1)}] \
    ==state.black_pawns[1].moves

    assert [{'position_after_move': (5, 5)}, {'position_after_move': (5, 3)}] \
    ==state.black_pawns[2].moves

    assert [{'position_after_move': (3, 5)}, {'position_after_move': (3, 3)}] \
    ==state.black_pawns[3].moves

def test_resolve_moves__queen_blocking_state(for_queen_blocking_pawns_state):
    state = for_queen_blocking_pawns_state
    move_res = MoveResolver(state)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)
    move_res.leave_max_beating_moves_only(state.white_pawns)
    move_res.leave_max_beating_moves_only(state.black_pawns)
    assert [{'beated_pawn_ids': [2, 3], 'position_after_move': (5, 7)}, {'beated_pawn_ids': [0, 4], 'position_after_move': (0, 2)}] \
    ==state.white_pawns[1].moves

    assert [{'beated_pawn_ids': [1], 'position_after_move': (5, 3)}] \
    ==state.black_pawns[0].moves

    assert [] \
    ==state.black_pawns[1].moves

    assert [] \
    ==state.black_pawns[2].moves

    assert [] \
    ==state.black_pawns[3].moves

    assert [] \
    ==state.black_pawns[4].moves

    assert [] \
    ==state.black_pawns[5].moves


def test_resolve_moves_for_all_collections__initial_state(initial_state):
    state = initial_state
    move_res = MoveResolver(state)

    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)

    for i in range(4,12):
        assert [] == state.white_pawns[i].moves

    assert [{'position_after_move': (4, 2)}, {'position_after_move': (4, 0)}]\
    == state.white_pawns[0].moves

    assert [{'position_after_move': (4, 4)}, {'position_after_move': (4, 2)}]\
    == state.white_pawns[1].moves

    assert [{'position_after_move': (4, 6)}, {'position_after_move': (4, 4)}]\
    == state.white_pawns[2].moves

    assert [{'position_after_move': (4, 6)}]\
    == state.white_pawns[3].moves

    for i in range(8):
        assert [] == state.black_pawns[i].moves

    assert [{'position_after_move': (3, 1)}]\
    == state.black_pawns[8].moves

    assert [{'position_after_move': (3, 3)}, {'position_after_move': (3, 1)}]\
    == state.black_pawns[9].moves

    assert [{'position_after_move': (3, 5)}, {'position_after_move': (3, 3)}]\
    == state.black_pawns[10].moves

    assert [{'position_after_move': (3, 7)}, {'position_after_move': (3, 5)}]\
    == state.black_pawns[11].moves

def test_resolve_moves_for_all_collections__different_pawns_around_white(different_pawns_around_white_state):
    state = different_pawns_around_white_state
    move_res = MoveResolver(state)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)

    assert [{'position_after_move': (1, 1), 'beated_pawn_ids': [0]}]\
    == state.white_pawns[1].moves

    assert [{'position_after_move': (1, 5)}, {'position_after_move': (1, 3)}]\
    == state.white_pawns[2].moves

    assert [{'beated_pawn_ids': [1], 'position_after_move': (4, 4)}]\
    == state.black_pawns[0].moves

    assert [{'position_after_move': (5, 3)}]\
    == state.black_pawns[1].moves

    assert [{'position_after_move': (6, 2)}, {'position_after_move': (6, 0)}]\
    == state.black_pawns[2].moves

    assert [{'position_after_move': (6, 6)}]\
    == state.black_pawns[3].moves

def test_resolve_moves_for_all_collections__extended_circle_state(extended_circle_state):
    state = extended_circle_state
    move_res = MoveResolver(state)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)

    assert [{'position_after_move': (5, 3), 'beated_pawn_ids': [1, 0, 3, 2]}]\
    == state.white_pawns[1].moves

    assert [{'beated_pawn_ids': [3, 2, 4], 'position_after_move': (7, 7)}]\
    == state.white_pawns[2].moves

    assert [{'position_after_move': (5, 1)}]\
    == state.white_pawns[3].moves

    assert [{'beated_pawn_ids': [5], 'position_after_move': (2, 0)}]\
    == state.white_pawns[4].moves

    assert [{'position_after_move': (3, 3)}, {'position_after_move': (3, 1)}]\
    ==state.black_pawns[0].moves

    assert [{'beated_pawn_ids': [1], 'position_after_move': (6, 4)}]\
    ==state.black_pawns[1].moves

    assert [{'beated_pawn_ids': [1], 'position_after_move': (6, 2)}]\
    ==state.black_pawns[2].moves

    assert [{'beated_pawn_ids': [2], 'position_after_move': (0, 6)}]\
    ==state.black_pawns[3].moves

    assert [{'position_after_move': (7, 7)}, {'position_after_move': (7, 5)}]\
    ==state.black_pawns[4].moves

    assert [{'position_after_move': (2, 0)}]\
    ==state.black_pawns[5].moves

    assert []\
    ==state.black_pawns[6].moves

def test_resolve_moves_for_all_collections__queen_extended_circle_state(queen_extended_circle_state):
    state = queen_extended_circle_state
    move_res = MoveResolver(state)
    move_res.resolve_moves_for_pawn_collection(state.black_pawns)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)

    assert [{'position_after_move': (5, 3), 'beated_pawn_ids': [2, 3, 0, 1]}]\
    ==state.white_pawns[1].moves

    assert [{'position_after_move': (1, 3), 'beated_pawn_ids': [3, 2, 1, 0]}]\
    ==state.white_pawns[2].moves

    assert [{'position_after_move': (1, 3), 'beated_pawn_ids': [0, 1, 2, 3]}]\
    ==state.white_pawns[3].moves

    assert [{'position_after_move': (3, 5), 'beated_pawn_ids': [2, 1, 0, 3]}]\
    ==state.white_pawns[4].moves

    assert [{'position_after_move': (3, 3)}, {'position_after_move': (3, 1)}]\
    ==state.black_pawns[0].moves

    assert [{'position_after_move': (5, 3)}, {'position_after_move': (5, 1)}]\
    ==state.black_pawns[1].moves

    assert [{'position_after_move': (5, 5)}, {'position_after_move': (5, 3)}]\
    ==state.black_pawns[2].moves

    assert [{'position_after_move': (3, 5)}, {'position_after_move': (3, 3)}]\
    ==state.black_pawns[3].moves


def test_resolve_moves_for_all_collections__queen_blocking_state(for_queen_blocking_pawns_state):
    state = for_queen_blocking_pawns_state
    move_res = MoveResolver(state)

    move_res.resolve_moves_for_pawn_collection(state.black_pawns)
    move_res.resolve_moves_for_pawn_collection(state.white_pawns)
    assert [{'beated_pawn_ids': [2, 3], 'position_after_move': (5, 7)}, {'beated_pawn_ids': [0, 4], 'position_after_move': (0, 2)}]\
    == state.white_pawns[1].moves

    assert [{'beated_pawn_ids': [1], 'position_after_move': (5, 3)}]\
    == state.black_pawns[0].moves

    assert [{'position_after_move': (3, 5)}, {'position_after_move': (3, 3)}]\
    == state.black_pawns[1].moves

    assert [{'position_after_move': (7, 5)}, {'position_after_move': (7, 3)}]\
    == state.black_pawns[2].moves

    assert [{'position_after_move': (7, 7)}, {'position_after_move': (7, 5)}]\
    == state.black_pawns[3].moves

    assert [{'position_after_move': (2, 2)}, {'position_after_move': (2, 0)}]\
    == state.black_pawns[4].moves

    assert [{'position_after_move': (2, 6)}]\
    == state.black_pawns[5].moves

def test_clean_opposite_moves(initial_state):
    state = initial_state
    move_res = MoveResolver()
    
    state = move_res.resolve_moves(state, 'white')
    assert len(state.white_pawns[1].moves) > 0
    assert len(state.black_pawns[9].moves) == 0

    state = move_res.resolve_moves(state, 'black')
    assert len(state.white_pawns[1].moves) == 0
    assert len(state.black_pawns[9].moves) > 0
