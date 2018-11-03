import pytest
from checkers.board import board as cb

def test_place_pawn_same_coin_on_field_and_state():
    """Checking on initialState case"""
    board = cb.Board()
    assert board.state.black_pawns[0] is board.fields[0][0]
    assert board.state.black_pawns[2] is not board.fields[0][0]
