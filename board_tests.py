import os
import unittest
import tempfile
from app import Board, BoardField, Coin,InvalidOperationError

class BoardTestCase(unittest.TestCase):
    
    def test_set_coin_y_x(self):
        board = Board()
        coin = Coin('white', 1)
        board.set_coin_y_x(coin, 2, 5)
        self.assertEquals(board.fields[2][5].coin, coin)
        self.assertEquals(coin.y, 2)
        self.assertEquals(coin.x, 5)

        with self.assertRaises(InvalidOperationError):
            board.set_coin_y_x(Coin('white', 9) , 0, 12)



if __name__ == '__main__':
    unittest.main()
