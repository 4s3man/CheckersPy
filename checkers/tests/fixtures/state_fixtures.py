import pytest
from checkers.board.state import *

def makeState(dict_state: dict):
    return State(json.dumps(dict_state))

@pytest.fixture
def initial_state():
    return InitialState()

@pytest.fixture
def one_coin_at_1_1():
    return makeState({
    "white_pawns":
        [
        {"y": 1, "x": 1,"color": "white", "type": "normal", "foreward": 1, "id": 0, "moves": []},
        None,
        None, None, None, None, None, None, None, None, None, None
        ],
    "black_pawns":
        [None, None, None, None, None, None, None, None, None, None, None, None]
    })

@pytest.fixture
def different_coins_around_white():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 3, "x": 3,"color": "white", "type": "normal", "foreward": -1, "id": 1, "moves": []},
            {"y": 2, "x": 4,"color": "white", "type": "normal", "foreward": -1, "id": 2, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
            ],
        "black_pawns":
            [
            {"y": 2, "x": 2,"color": "black", "type": "normal", "foreward": 1, "id": 0, "moves": []},
            {"y": 4, "x": 2,"color": "black", "type": "normal", "foreward": 1, "id": 1, "moves": []},
            {"y": 5, "x": 1,"color": "black", "type": "normal", "foreward": 1, "id": 2, "moves": []},
            {"y": 5, "x": 7,"color": "black", "type": "normal", "foreward": 1, "id": 3, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })
