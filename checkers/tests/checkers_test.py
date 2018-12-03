import pytest
from checkers.checkers import *

def test_make_move(extended_circle_state):
    checkers = Checkers(extended_circle_state)
    checkers.resolve_moves('white')
    pawn = checkers.state.white_pawns[1]

    checkers.make_move(pawn.id, pawn.color, pawn.moves[0])
    """Assert pawn moved"""
    assert checkers.state.white_pawns[1].y == 5 and checkers.state.white_pawns[1].x == 3
    """Assert beat enemy pawns"""
    for enemy_id in pawn.moves[0]['beated_pawn_ids']:
        assert checkers.state.black_pawns[enemy_id] == None

    checkers.resolve_moves('black')
    pawn_to_queen = checkers.state.black_pawns[4]

    checkers.make_move(pawn_to_queen.id, pawn_to_queen.color, pawn_to_queen.moves[0])
    assert checkers.state.black_pawns[4].y == 7 and checkers.state.black_pawns[4].x == 7
    assert checkers.state.black_pawns[4].type == 'queen'
