import pytest
from modules.Board import *

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

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
