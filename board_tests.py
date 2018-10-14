import os
import unittest
import tempfile
from app import Board

class BoardTestCase(unittest.TestCase):

    def test_working(self):
        board = Board()


if __name__ == '__main__':
    unittest.main()
