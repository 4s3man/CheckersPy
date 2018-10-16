import os
import unittest
import tempfile
import json
from app import Board, BoardField, Coin,InvalidOperationError

class BoardTestCase(unittest.TestCase):

    #todo
    def test_set_coins_from_json(self):
        board = Board()
        coin = Coin('white', 0)
        board.set_coin_y_x(coin, 2, 4)
        coin.set_foreward_vector(-1)
        board.white_coins.append(coin)
        json = board.json_encode_coins()

        board1 = Board()
        board1.set_coins_from_json(json)
        print(board1.white_coins)


    def test_set_coin_y_x(self):
        board = Board()
        coin = Coin('white', 1)
        board.set_coin_y_x(coin, 2, 5)
        self.assertEqual(board.fields[2][5].coin, coin)
        self.assertEqual(coin.y, 2)
        self.assertEqual(coin.x, 5)

        with self.assertRaises(InvalidOperationError):
            board.set_coin_y_x(Coin('white', 9) , 0, 12)

    def test_enemy_coin_in_this_direction(self):
        board = Board()
        coin = Coin('white', 1)
        coin1 = Coin('black', 1)
        board.set_coin_y_x(coin, 3, 1)
        board.set_coin_y_x(coin1, 4, 0)
        board.set_coin_y_x(Coin('black', 1), 2, 2)
        board.set_coin_y_x(Coin('white', 1), 4, 2)
        board.set_coin_y_x(Coin('white', 1), 2, 0)

        #assert white recognizes enemies
        self.assertTrue(board.enemy_in_this_direction(coin, (-1, 1)))
        self.assertTrue(board.enemy_in_this_direction(coin, (1, -1)))
        self.assertFalse(board.enemy_in_this_direction(coin, (-1, -1)))
        self.assertFalse(board.enemy_in_this_direction(coin, (1, 1)))
        #assert black recognizes enemies
        self.assertTrue(board.enemy_in_this_direction(coin1, (-1, 1)))
        #assert no enemy if out of the board
        self.assertFalse(board.enemy_in_this_direction(coin1, (-1, -1)))

    def test_can_jump_in_direction(self):
        board = Board()
        coin = Coin('white', 1)
        coin1 = Coin('black', 1)
        board.set_coin_y_x(coin, 3, 1)
        board.set_coin_y_x(coin1, 4, 0)
        board.set_coin_y_x(Coin('black', 1), 2, 2)
        board.set_coin_y_x(Coin('black', 1), 4, 2)
        board.set_coin_y_x(Coin('black', 1), 5, 3)

        #can jump
        self.assertTrue(board.can_jump_in_direction(coin, (-1,1)))

        #cant jump becouse next field is not free
        self.assertFalse(board.can_jump_in_direction(coin, (1,1)))

        #cant jump becouse next field is out of range
        self.assertFalse(board.can_jump_in_direction(coin, (1, -1)))

if __name__ == '__main__':
    unittest.main()
