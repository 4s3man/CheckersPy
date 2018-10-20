import os
import unittest
import tempfile
import json
from app import Board, BoardField, Coin, Move, BoardError, NoCoinError

class BoardTestCase(unittest.TestCase):

    #todo
    def test_set_coins_from_json(self):
        board = Board()
        coin = Coin('white', 0)
        board.set_coin_y_x(coin, 2, 4)
        coin.set_foreward_vector(-1)
        board.white_coins[coin.id] = coin
        json = board.json_encode_coins()

        # print(json)
        board1 = Board()
        board1.set_coins_from_json(json)
        self.assertEqual(board.white_coins[coin.id].__dict__, board1.white_coins[coin.id].__dict__)

        board1.white_coins[coin.id].set_foreward_vector(1)
        self.assertNotEqual(board.white_coins[coin.id].__dict__, board1.white_coins[coin.id].__dict__)

    def test_set_coin_y_x(self):
        board = Board()
        coin = Coin('white', 1)
        board.set_coin_y_x(coin, 2, 5)
        self.assertEqual(board.fields[2][5].coin, coin)
        self.assertEqual(coin.y, 2)
        self.assertEqual(coin.x, 5)

        self.assertEqual(board.white_coins[coin.id], coin)

        with self.assertRaises(BoardError):
            board.set_coin_y_x(Coin('white', 9) , 0, 12)

    def test_unset_coin(self):
        board = Board()
        coin = Coin('white', 1)
        y,x = 3,3

        board.set_coin_y_x(coin, y, x)
        board.unset_coin(coin)

        self.assertFalse(board.white_coins[1])
        self.assertEqual(None, board.fields[y][x].coin)


    #todo
    def test_get_coin_in_direction(self):
        board = Board()
        coin = Coin('white', 1)
        coin1 = Coin('black', 1)
        board.set_coin_y_x(coin, 3, 1)
        board.set_coin_y_x(coin1, 4, 0)
        board.set_coin_y_x(Coin('black', 2), 2, 2)
        board.set_coin_y_x(Coin('white', 2), 4, 2)


        #returns coin
        self.assertTrue(isinstance(board.get_coin_in_direction(coin, (1,1)), Coin))
        self.assertTrue(isinstance(board.get_coin_in_direction(coin1, (-1,1)), Coin))

        #raise NoCoinError if no coin in direciton
        with self.assertRaises(NoCoinError):
            board.get_coin_in_direction(coin, (-1,-1))

        #raises BoardError in case of direction is out of the board
        with self.assertRaises(BoardError):
            board.get_coin_in_direction(coin1, (1, -1))

        with self.assertRaises(NoCoinError):
            board.set_coin_y_x(coin1, 5, 1)
            board.get_coin_in_direction(coin1, (1,1))


    def test_have_obligatory_move(self):
        board = Board()
        coin = Coin('white', 1)
        coin1 = Coin('black', 1)
        board.set_coin_y_x(coin, 3, 3)

        """When coin was already beated"""
        board.set_coin_y_x(coin1, 2, 2)
        move = Move()
        move.beated_coins.append(coin1)
        self.assertFalse(board.have_obligatory_move(coin, move))

        """Check move in any direction"""
        move = None
        board.unset_coin(coin1)
        board.set_coin_y_x(coin1, 2, 2)
        self.assertTrue(board.have_obligatory_move(coin, move))

        board.set_coin_y_x(Coin('black', 1), 2, 3)
        self.assertTrue(board.have_obligatory_move(coin, move))

        board.set_coin_y_x(Coin('black', 1), 4, 2)
        self.assertTrue(board.have_obligatory_move(coin, move))

        board.set_coin_y_x(Coin('black', 1), 4, 4)
        self.assertTrue(board.have_obligatory_move(coin, move))


if __name__ == '__main__':
    unittest.main()
