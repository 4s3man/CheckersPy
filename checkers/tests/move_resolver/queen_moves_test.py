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
