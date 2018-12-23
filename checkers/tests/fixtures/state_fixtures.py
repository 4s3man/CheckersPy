import pytest
from checkers.board.state import *

def makeState(dict_state: dict):
    return State(json.dumps(dict_state))

@pytest.fixture
def initial_state():
    return InitialState()

@pytest.fixture
def one_pawn_at_1_1_state():
    return makeState({
    "white_pawns":
        [
        {"y": 1, "x": 1,"color": "white", "type": "normal", "foreward": -1, "id": 0, "moves": []},
        null,
        None, None, None, None, None, None, None, None, None, None
        ],
    "black_pawns":
        [None, None, None, None, None, None, None, None, None, None, None, None]
    })

@pytest.fixture
def different_pawns_around_white_state():
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

@pytest.fixture
def extended_circle_state():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 5, "x": 3,"color": "white", "type": "normal", "foreward": -1, "id": 1, "moves": []},
            {"y": 1, "x": 5,"color": "white", "type": "normal", "foreward": -1, "id": 2, "moves": []},
            {"y": 6, "x": 0,"color": "white", "type": "normal", "foreward": -1, "id": 3, "moves": []},
            {"y": 0, "x": 2,"color": "white", "type": "normal", "foreward": -1, "id": 4, "moves": []},
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
            {"y": 4, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 2, "moves": []},
            {"y": 2, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 3, "moves": []},
            {"y": 6, "x": 6,"color": "black", "type": "normal", "foreward": 1, "id": 4, "moves": []},
            {"y": 1, "x": 1,"color": "black", "type": "normal", "foreward": 1, "id": 5, "moves": []},
            {"y": 7, "x": 3,"color": "black", "type": "normal", "foreward": 1, "id": 6, "moves": []},
            None,
            None,
            None,
            None,
            None]
    })

@pytest.fixture
def for_queen_state():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 4, "x": 2,"color": "white", "type": "queen", "foreward": -1, "id": 1, "moves": []},
            None,
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
            {"y": 2, "x": 0,"color": "black", "type": "normal", "foreward": 1, "id": 0, "moves": []},
            {"y": 2, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 1, "moves": []},
            {"y": 6, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 2, "moves": []},
            {"y": 6, "x": 6,"color": "black", "type": "normal", "foreward": 1, "id": 3, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })

@pytest.fixture
def for_queen_blocking_pawns_state():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 4, "x": 2,"color": "white", "type": "queen", "foreward": -1, "id": 1, "moves": []},
            None,
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
            {"y": 3, "x": 1,"color": "black", "type": "normal", "foreward": 1, "id": 0, "moves": []},
            {"y": 2, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 1, "moves": []},
            {"y": 6, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 2, "moves": []},
            {"y": 6, "x": 6,"color": "black", "type": "normal", "foreward": 1, "id": 3, "moves": []},
            {"y": 1, "x": 1,"color": "black", "type": "normal", "foreward": 1, "id": 4, "moves": []},
            {"y": 1, "x": 5,"color": "black", "type": "normal", "foreward": 1, "id": 5, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })

@pytest.fixture
def for_queen_normal_moves_state():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 4, "x": 2,"color": "white", "type": "queen", "foreward": -1, "id": 1, "moves": []},
            None,
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
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })

@pytest.fixture
def queen_extended_circle_state():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 7, "x": 1,"color": "white", "type": "queen", "foreward": -1, "id": 1, "moves": []},
            {"y": 0, "x": 2,"color": "white", "type": "queen", "foreward": -1, "id": 2, "moves": []},
            {"y": 0, "x": 4,"color": "white", "type": "queen", "foreward": -1, "id": 3, "moves": []},
            {"y": 1, "x": 7,"color": "white", "type": "queen", "foreward": -1, "id": 4, "moves": []},
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
            {"y": 4, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 2, "moves": []},
            {"y": 2, "x": 4,"color": "black", "type": "normal", "foreward": 1, "id": 3, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })

@pytest.fixture
def no_blocked_beating_move_bug():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 2, "x": 4,"color": "white", "type": "queen", "foreward": -1, "id": 1, "moves": []},
            None,
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
            {"y": 3, "x": 1,"color": "black", "type": "normal", "foreward": 1, "id": 0, "moves": []},
            {"y": 3, "x": 3,"color": "black", "type": "normal", "foreward": 1, "id": 1, "moves": []},
            None,
            None,
            {"y": 1, "x": 1,"color": "black", "type": "normal", "foreward": 1, "id": 4, "moves": []},
            {"y": 1, "x": 5,"color": "black", "type": "normal", "foreward": 1, "id": 5, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })

@pytest.fixture
def only_queens_state():
    return makeState({
        "white_pawns":
            [
            None,
            {"y": 4, "x": 2,"color": "white", "type": "queen", "foreward": -1, "id": 1, "moves": []},
            None,
            {"y": 5, "x": 1,"color": "white", "type": "queen", "foreward": -1, "id": 3, "moves": []},
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
            {"y": 3, "x": 1,"color": "black", "type": "queen", "foreward": 1, "id": 0, "moves": []},
            {"y": 2, "x": 4,"color": "black", "type": "queen", "foreward": 1, "id": 1, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })
@pytest.fixture
def black_win_state():
    return makeState({
        "white_pawns":
            [
            None,
            None,
            None,
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
            {"y": 3, "x": 1,"color": "black", "type": "queen", "foreward": 1, "id": 0, "moves": []},
            {"y": 2, "x": 4,"color": "black", "type": "queen", "foreward": 1, "id": 1, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None]
    })
@pytest.fixture
def white_win_state():
    return makeState({
        "white_pawns":
            [
            {"y": 3, "x": 1,"color": "white", "type": "queen", "foreward": 1, "id": 0, "moves": []},
            {"y": 2, "x": 4,"color": "white", "type": "queen", "foreward": 1, "id": 1, "moves": []},
            None,
            None,
            None,
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
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
            ]
    })
@pytest.fixture
def two_queens_state():
    return makeState({
        "white_pawns":
            [
            {"y": 3, "x": 1,"color": "white", "type": "queen", "foreward": 1, "id": 0, "moves": []},
            None,
            None,
            None,
            None,
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
            {"y": 4, "x": 6,"color": "black", "type": "queen", "foreward": 1, "id": 0, "moves": []},
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
            ]
    })
@pytest.fixture
def no_moves_for_black():
    return State('{"white_pawns": [{"color": "white", "id": 0, "type": "queen", "x": 1, "y": 1, "foreward": -1, "moves": []}, null, null, {"color": "white", "id": 3, "type": "normal", "x": 7, "y": 3, "foreward": -1, "moves": []}, null, null, {"color": "white", "id": 6, "type": "normal", "x": 3, "y": 5, "foreward": -1, "moves": []}, {"color": "white", "id": 7, "type": "normal", "x": 7, "y": 5, "foreward": -1, "moves": []}, {"color": "white", "id": 8, "type": "normal", "x": 1, "y": 7, "foreward": -1, "moves": []}, {"color": "white", "id": 9, "type": "normal", "x": 5, "y": 3, "foreward": -1, "moves": []}, {"color": "white", "id": 10, "type": "normal", "x": 6, "y": 6, "foreward": -1, "moves": []}, {"color": "white", "id": 11, "type": "normal", "x": 7, "y": 7, "foreward": -1, "moves": []}], "black_pawns": [null, null, null, null, null, null, null, null, {"color": "black", "id": 8, "type": "normal", "x": 0, "y": 6, "foreward": 1, "moves": []}, null, null, null], "winner": ""}')
