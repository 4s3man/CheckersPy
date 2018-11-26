import pytest
from helpers.connection import *

def test_receive_pawn_move():
    goodMove1 =  {'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 6]}}
    assert goodMove1 == receive_pawn_move(goodMove1)

    goodMove2 =  {'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 6], 'beated_pawn_ids':[1,2,3]}}
    assert goodMove2 == receive_pawn_move(goodMove2)

    emptyMove = {}
    with pytest.raises(EmptyPawnMove):
        assert receive_pawn_move(emptyMove)

    invalidMoves = {
        'tooLongMoveData': {'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 6]}, 'badThings':[1,2,3]},
        'badId': {'id': -1, 'color': 'white', 'move': {'position_after_move': [4, 6]}},
        'badColor': {'id': 3, 'color': 'green', 'move': {'position_after_move': [4, 6]}},
        'badPosition': {'id': 3, 'color': 'green', 'move': {'position_after_move': [4, 9]}},
        'badBeatedCoinsIds': {'id': 3, 'color': 'green', 'move': {'position_after_move': [4, 9], 'beated_pawn_ids':[13]}}
    }
    for key, value in invalidMoves.items():
        with pytest.raises(InvalidPawnMove):
            assert receive_pawn_move(value)
