import pytest
import json
from checkers.board import board as cb

@pytest.fixture
def state_1coin():
    state = cb.State()
    state.white_pawns[2] = cb.Pawn('white', 2)
    state.white_pawns[2].set_positon((1,1))
    state.white_pawns[2].set_foreward_vector(1)
    state.white_pawns[2].moves = {'beated_coin_ids':[1,2,3,4], "fields": [(1,2), (3,4)]}
    return state

# def test_json_encode_state_coin1(state_1coin):
#     json_state_1 = {'black_pawns': [None, None, None, None, None, None, None, None, None, None, None, None], 'white_pawns': [None, {'color': 'white', 'x': 1, 'y': 1, 'id': 2, 'type': 'normal', 'moves': {'beated_coin_ids': [1, 2, 3, 4], 'fields': [[1, 2], [3, 4]]}}, None, None, None, None, None, None, None, None, None, None]}
#     assert json_state_1 == json.loads(state_1coin.json_encode())
#
# def test_json_encode_initialState():
#     state = cb.InitialState()
#     json_initial_state_fixture = {'white_pawns': [{'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 1, 'y': 5, 'id': 0}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 3, 'y': 5, 'id': 1}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 5, 'y': 5, 'id': 2}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 7, 'y': 5, 'id': 3}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 0, 'y': 6, 'id': 4}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 2, 'y': 6, 'id': 5}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 4, 'y': 6, 'id': 6}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 6, 'y': 6, 'id': 7}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 1, 'y': 7, 'id': 8}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 3, 'y': 7, 'id': 9}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 5, 'y': 7, 'id': 10}, {'type': 'normal', 'foreward': -1, 'color': 'white', 'x': 7, 'y': 7, 'id': 11}], 'black_pawns': [{'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 0, 'y': 0, 'id': 0}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 2, 'y': 0, 'id': 1}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 4, 'y': 0, 'id': 2}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 6, 'y': 0, 'id': 3}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 1, 'y': 1, 'id': 4}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 3, 'y': 1, 'id': 5}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 5, 'y': 1, 'id': 6}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 7, 'y': 1, 'id': 7}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 0, 'y': 2, 'id': 8}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 2, 'y': 2, 'id': 9}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 4, 'y': 2, 'id': 10}, {'type': 'normal', 'foreward': 1, 'color': 'black', 'x': 6, 'y': 2, 'id': 11}]}
#     assert json_initial_state_fixture == json.loads(state.json_encode())

def test_json_decode(state_1coin):
    json_state_1 = {'black_pawns': [None, None, None, None, None, None, None, None, None, None, None, None], 'white_pawns': [None, {'color': 'white', 'x': 1, 'y': 1, 'id': 2, 'type': 'normal', 'moves': {'beated_coin_ids': [1, 2, 3, 4], 'fields': [[1, 2], [3, 4]]}}, None, None, None, None, None, None, None, None, None, None]}
    state = cb.State(state_1coin.json_encode())
    assert json.dumps(state.json_encode()) == json.dumps(state_1coin.json_encode())
