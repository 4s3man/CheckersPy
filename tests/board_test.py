import pytest
from checkers.board.board import *

def test_place_pawns():
    """Checking on initialState case"""
    state = InitialState()
    board = Board(state)
    for pawn in state.black_pawns:
        assert state.black_pawns[pawn.id] is board.fields[pawn.y][pawn.x]
    for pawn in state.white_pawns:
        assert state.white_pawns[pawn.id] is board.fields[pawn.y][pawn.x]

def test_has_position():
    board = Board()
    assert True == board.has_position(0,0)
    assert True == board.has_position(7,7)

    assert False == board.has_position(-1,0)
    assert False == board.has_position(8,7)
