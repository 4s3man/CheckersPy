import unittest
from app import Board, BoardField, Coin, Move, BoardError, NoCoinError

def readable_moves(moves):
    return ['pos_yx: ' + str(move['pos']) + 'beated_coins_yx: ' + str([(coin.x, coin.y) for coin in move['beated_coins']]) for move in moves]
def compare_moves(should_return, coin_moves):
    if 'obligatory' in coin_moves and 'obligatory' not in should_return: return False
    return True

def calc_beated_coins_from_pos(board, coin, pos):
    coins = []
    for y, x in pos:
        v = (coin.y - y, coin.x - x)

class GetMovesForCoinTestCase(unittest.TestCase):
    def test_jump_down_extended(self):
            board = Board()
            black_coins = [Coin('black', i) for i in range(5)]
            coin = Coin('white', 2)
            coin.set_foreward_vector(-1)
            board.set_coin_y_x(coin, 1, 5)
            board.set_coin_y_x(black_coins[0], 2, 4)
            board.set_coin_y_x(black_coins[1], 4, 4)
            board.set_coin_y_x(black_coins[2], 4, 2)
            board.set_coin_y_x(black_coins[3], 6, 6)

            # should_return = {'obligatory': [
            # {'beated_coins': [0,1,2], 'pos': [(3, 3), (5, 5), (7, 7)]},
            # {'beated_coins': [0,1], 'pos': [(3, 3), (5, 1)]}]}
            board.get_moves_for_coin(coin)
            print(coin.moves)
            # self.assertEqual(readable_moves(moves), readable_moves(should_return))


if __name__ == '__main__':
    unittest.main()
