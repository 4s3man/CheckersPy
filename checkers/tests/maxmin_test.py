import pytest
from checkers.maxmin import *
from checkers.checkers import *

def test_make_moves_gen(for_max_min_test_simple):
    state = for_max_min_test_simple
    # state = initial_state()

    checkers = Checkers(state)
    checkers.resolve_moves('white')

    move = iter(make_moves_gen(state.white_pawns))
    assert next(move) == [{'id': 1, 'color': 'white', 'move': {'position_after_move': [4, 4]}}, 0]
    assert next(move) == [{'id': 1, 'color': 'white', 'move': {'position_after_move': [4, 2]}}, 0]
    assert next(move) == [{'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 2]}}, 0]
    assert next(move) == [{'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 0]}}, 0]

def test_make_moves_with_scores(for_max_min_test_simple):
    state = for_max_min_test_simple
    moves = make_moves_with_scores(state, 'white')

    move = iter(moves)
    assert next(move) == [{'id': 1, 'color': 'white', 'move': {'position_after_move': [4, 4]}}, 2]
    assert next(move) == [{'id': 1, 'color': 'white', 'move': {'position_after_move': [4, 2]}}, -1]
    assert next(move) == [{'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 2]}}, 0]
    assert next(move) == [{'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 0]}}, 2]

    moves = make_moves_with_scores(state, 'black')
    move = iter(moves)
    assert next(move) == [{'id': 0, 'color': 'black', 'move': {'position_after_move': [4, 2]}}, -30]
    assert next(move) == [{'id': 0, 'color': 'black', 'move': {'position_after_move': [4, 0]}}, 1]
    assert next(move) == [{'id': 1, 'color': 'black', 'move': {'position_after_move': [3, 5]}}, 1]
    assert next(move) == [{'id': 1, 'color': 'black', 'move': {'position_after_move': [3, 3]}}, 1]
