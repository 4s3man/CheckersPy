import pytest
from modules.Board import *
from tests.helpers import *

def test_dono():
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

board.get_moves_for_coin(coin)


# make_beated_coins_from_pos(board, coin)
# def make_beated_coins_from_pos(board, coin):
    # for move in coin.moves['obligatory']:
    #     all_poses = []
    #     all_poses = [(coin.y, coin.x)] + move['pos']
    #     print(move['pos'])
        # for i in range(len(move['pos'])):
            # print(all_poses[i])
