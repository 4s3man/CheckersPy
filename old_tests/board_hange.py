import pytest
from modules.Board import *
from tests.helpers import *

def test_set_coins_from_json():
    board = Board()
    coin = Coin('white', 0)
    board.set_coin_y_x(coin, 2, 4)
    coin.set_foreward_vector(-1)
    board.white_coins[coin.id] = coin
    json = board.json_encode_coins()

    # print(json)
    board1 = Board()
    board1.set_coins_from_json(json)
    assert board.white_coins[coin.id].__dict__ == board1.white_coins[coin.id].__dict__

    board1.white_coins[coin.id].set_foreward_vector(1)
    assert board.white_coins[coin.id].__dict__ != board1.white_coins[coin.id].__dict__

def test_set_coin_y_x():
    board = Board()
    coin = Coin('white', 1)
    board.set_coin_y_x(coin, 2, 5)
    assert board.fields[2][5].coin == coin
    assert coin.y == 2
    assert coin.x == 5

    assert board.white_coins[coin.id] == coin

    with pytest.raises(BoardError):
        board.set_coin_y_x(Coin('white', 9) , 0, 12)

def test_unset_coin():
    board = Board()
    coin = Coin('white', 1)
    y,x = 3,3

    board.set_coin_y_x(coin, y, x)
    board.unset_coin(coin)

    assert None == board.white_coins[1]
    assert None == board.fields[y][x].coin

def test_get_coin_in_direction():
    board = Board()
    coin = Coin('white', 1)
    coin1 = Coin('black', 1)
    board.set_coin_y_x(coin, 3, 1)
    board.set_coin_y_x(coin1, 4, 0)
    board.set_coin_y_x(Coin('black', 2), 2, 2)
    board.set_coin_y_x(Coin('white', 2), 4, 2)

    #returns coin
    assert True == isinstance(board.get_coin_in_direction(coin, (1,1)), Coin)
    assert True == isinstance(board.get_coin_in_direction(coin1, (-1,1)), Coin)

    #raise NoCoinError if no coin in direciton
    with pytest.raises(NoCoinError):
        board.get_coin_in_direction(coin, (-1,-1))

    #raises BoardError in case of direction is out of the board
    with pytest.raises(BoardError):
        board.get_coin_in_direction(coin1, (1, -1))

    with pytest.raises(NoCoinError):
        board.set_coin_y_x(coin1, 5, 1)
        board.get_coin_in_direction(coin1, (1,1))

def test_have_obligatory_move():
    board = Board()
    coin = Coin('white', 1)
    coin1 = Coin('black', 1)
    board.set_coin_y_x(coin, 3, 3)

    """When coin was already beated"""
    board.set_coin_y_x(coin1, 2, 2)
    move = {'beated_coins':[]}
    move['beated_coins'].append(coin1)
    assert False == board.have_obligatory_move(coin, move)

    """Check move in any direction"""
    move = None
    board.unset_coin(coin1)
    board.set_coin_y_x(coin1, 2, 2)
    assert True == board.have_obligatory_move(coin, move)

    board.set_coin_y_x(Coin('black', 1), 2, 3)
    assert True == board.have_obligatory_move(coin, move)

    board.set_coin_y_x(Coin('black', 1), 4, 2)
    assert True == board.have_obligatory_move(coin, move)

    board.set_coin_y_x(Coin('black', 1), 4, 4)
    assert True == board.have_obligatory_move(coin, move)

def test_have_obligatory_move_after_move():
        board = Board()
        black_coins = [Coin('black', i) for i in range(4)]
        coin = Coin('white', 2)
        board.set_coin_y_x(coin, 3, 3)
        board.set_coin_y_x(black_coins[0], 2, 2)
        board.set_coin_y_x(black_coins[1], 4, 4)
        board.set_coin_y_x(black_coins[2], 2, 4)

        move = {'beated_coins':[black_coins[1]]}
        assert True == board.have_obligatory_move(coin, move)

def test_get_obligatory_moves():
    board = Board()
    black_coins = [Coin('black', i) for i in range(4)]
    coin = Coin('white', 2)
    board.set_coin_y_x(coin, 3, 3)
    board.set_coin_y_x(black_coins[0], 2, 2)
    board.set_coin_y_x(black_coins[1], 4, 4)
    board.set_coin_y_x(black_coins[2], 2, 4)
    board.set_coin_y_x(black_coins[3], 6, 6)

    moves = board.get_obligatory_moves(coin, [])
    should_return = [
    {'pos': [(5, 5), (7, 7)], 'beated_coins': [black_coins[1], black_coins[3]]},
    {'pos': [(1, 5)], 'beated_coins': [black_coins[2]]},
    {'pos': [(1, 1)], 'beated_coins': [black_coins[0]]}
    ]

    assert readable_moves(moves) == readable_moves(should_return)

def test_get_obligatory_moves_1():
    board = Board()
    black_coins = [Coin('black', i) for i in range(4)]
    coin = Coin('white', 2)
    board.set_coin_y_x(coin, 5, 5)
    board.set_coin_y_x(black_coins[0], 2, 2)
    board.set_coin_y_x(black_coins[1], 4, 4)
    board.set_coin_y_x(black_coins[2], 2, 4)

    moves = board.get_obligatory_moves(coin, [])
    should_return = [
    {'beated_coins': [black_coins[1], black_coins[2] ], 'pos': [(3, 3), (1, 5)]},
    {'beated_coins': [black_coins[1], black_coins[0]], 'pos': [(3, 3), (1, 1)]}
    ]
    assert readable_moves(moves) == readable_moves(should_return)

def test_get_obligatory_moves_extended_circle_example():
    board = Board()
    black_coins = [Coin('black', i) for i in range(5)]
    coin = Coin('white', 2)
    coin.set_foreward_vector(1)
    board.set_coin_y_x(coin, 5, 3)
    board.set_coin_y_x(black_coins[0], 4, 4)
    board.set_coin_y_x(black_coins[1], 2, 4)
    board.set_coin_y_x(black_coins[2], 2, 2)
    board.set_coin_y_x(black_coins[3], 4, 2)
    board.set_coin_y_x(black_coins[4], 6, 4)

    should_return = [
    {'beated_coins': [black_coins[4]], 'pos': [(7, 5)]},
    {'beated_coins': black_coins, 'pos': [(3, 5), (1, 3), (3, 1), (5, 3), (7, 5)]}]

    moves = board.get_obligatory_moves(coin, [])
    assert readable_moves(moves) == readable_moves(should_return)

def test_same_pos_in_movelist():
    board = Board()
    poses = [{'pos': [(7, 5)]}, {'pos': [(3, 5), (1, 3), (3, 1), (5, 3), (7, 5)]}]
    move = {'pos': [(3, 1), (1, 3), (3, 5), (5, 3), (7, 5)]}
    assert True == board.same_pos_in_movelist(move, poses)
    move['pos'].pop()
    assert False == board.same_pos_in_movelist(move, poses)
