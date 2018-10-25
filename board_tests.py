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
        move = {'beated_coins':[]}
        move['beated_coins'].append(coin1)
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

    def test_have_obligatory_move__after_move(self):
            board = Board()
            black_coins = [Coin('black', i) for i in range(4)]
            coin = Coin('white', 2)
            board.set_coin_y_x(coin, 3, 3)
            board.set_coin_y_x(black_coins[0], 2, 2)
            board.set_coin_y_x(black_coins[1], 4, 4)
            board.set_coin_y_x(black_coins[2], 2, 4)

            move = {'beated_coins':[black_coins[1]]}
            self.assertTrue(board.have_obligatory_move(coin, move))


    def test_get_obligatory_moves(self):
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

        self.assertEqual(self.readable_moves(moves), self.readable_moves(should_return))

    def test_get_obligatory_moves_1(self):
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
        self.assertEqual(self.readable_moves(moves), self.readable_moves(should_return))

    def test_get_obligatory_moves_extended_circle_example(self):
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
        self.assertEqual(self.readable_moves(moves), self.readable_moves(should_return))

    def test_same_pos_in_movelist(self):
        board = Board()
        poses = [{'pos': [(7, 5)]}, {'pos': [(3, 5), (1, 3), (3, 1), (5, 3), (7, 5)]}]
        move = {'pos': [(3, 1), (1, 3), (3, 5), (5, 3), (7, 5)]}
        self.assertTrue(board.same_pos_in_movelist(move, poses))
        move['pos'].pop()
        self.assertFalse(board.same_pos_in_movelist(move, poses))


    def readable_moves(self, moves):
        return ['pos_yx: ' + str(move['pos']) + 'beated_coins_yx: ' + str([(coin.x, coin.y) for coin in move['beated_coins']]) for move in moves]

if __name__ == '__main__':
    unittest.main()
