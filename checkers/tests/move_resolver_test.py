import pytest
from checkers.board.move_resolver import *

def test_get_pawn_in_direction(different_coins_around_white):
    state = different_coins_around_white
    pawn = state.white_pawns[1]
    border_pawn = state.black_pawns[3]
    move_res = MoveResolver(state)

    assert state.black_pawns[0] is move_res.get_pawn_in_direction(pawn, -1, -1)
    assert state.black_pawns[0] is not move_res.get_pawn_in_direction(pawn, -1, 1)

    assert state.white_pawns[2] is move_res.get_pawn_in_direction(pawn, -1, 1)
    assert state.white_pawns[1] is not move_res.get_pawn_in_direction(pawn, -1, 1)

    with pytest.raises(NoCoinError):
        assert move_res.get_pawn_in_direction(pawn, 1, 1)

    with pytest.raises(OutOfBoardError):
        assert move_res.get_pawn_in_direction(border_pawn, -1, 1)
