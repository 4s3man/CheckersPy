import pytest
from checkers.board.state import *

@pytest.fixture
def initial_state():
    return InitialState()

@pytest.fixture
def one_white_coin_at_1_1():
    state = State()
    state.white_pawns[1] = Pawn('white', 2)
    state.white_pawns[1].set_positon(1,1)
    state.white_pawns[1].set_foreward_vector(1)
    state.white_pawns[1].moves = {'beated_coin_ids':[1,2,3,4], "fields": [(1,2), (3,4)]}

    return state
