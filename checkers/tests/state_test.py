import pytest
import json
import copy
from checkers.board.state import *

@pytest.fixture
def state_1coin():
    state = State()
    state.white_pawns[2] = Pawn('white', 2)
    state.white_pawns[2].set_positon(1,1)
    state.white_pawns[2].set_foreward_vector(1)
    state.white_pawns[2].moves = {'beated_coin_ids':[1,2,3,4], "fields": [(1,2), (3,4)]}
    return copy.deepcopy(state)

def test_state_eq_(state_1coin):
    s1 = copy.deepcopy(state_1coin)
    initialState = InitialState()
    assert s1 == state_1coin
    assert s1 != initialState

def test_json_decode(state_1coin):
    state = State(state_1coin.json_encode())
    initialState = InitialState()
    assert state == state_1coin
    assert state != initialState
