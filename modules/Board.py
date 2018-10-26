import json
import itertools
import copy
from modules.Coin import *
from modules.BoardField import *

class BoardError(Exception):
    pass

class NoCoinError(BoardError):
    pass

class OutOfBoardError(BoardError):
    pass

class Board:
    board_size = 8
    coins_for_site = 12
    def __init__(self):
        self.fields = [[BoardField() for x in range(self.board_size)] for y in range(self.board_size)]
        self.white_coins = [None] * self.coins_for_site
        self.black_coins = [None] * self.coins_for_site

    def set_coin_y_x(self, coin, y, x):
        if self.field_in_board(y, x):
            self.fields[y][x].set_coin(coin, y, x)
            coins = self.white_coins if coin.color == 'white' else self.black_coins
            coins[coin.id] = coin
        else:
            raise BoardError("Wanted to set coin out of the board")

    def unset_coin(self, coin):
        coins = self.white_coins if coin.color == 'white' else self.black_coins
        coins[coin.id] = None
        self.fields[coin.y][coin.x].unset_coin()

    def set_initial_state(self):
        self.white_coins = [Coin('white', id) for id in range(self.coins_for_site)]
        self.black_coins = [Coin('black', id) for id in range(self.coins_for_site)]

        black_fields = ((self.board_size**2)//2)
        down_coins, up_coins = iter(self.white_coins), iter(self.black_coins)
        for i in range(black_fields):
            y = i//(self.board_size//2)
            x = (i%4)*2 + y%2
            try:
                if y in range(0,3):
                    coin = next(up_coins)
                    self.set_coin_y_x(coin, y, x)
                    coin.set_foreward_vector(1)
                if y in range(5,8):
                    coin = next(down_coins)
                    self.set_coin_y_x(coin, y, x)
                    coin.set_foreward_vector(-1)
            except StopIteration:
                pass

    def json_encode_coins(self):
        coins = {
            'white_coins': self.white_coins,
            'black_coins': self.black_coins}
        return json.dumps(coins, default=(lambda x: x.__dict__))

        #przetestować bo po dodaniu coin.foreward powinno być zepsute
    def set_coins_from_json(self, json_coins):
        coins = json.loads(json_coins)
        for name, arr in coins.items():
            collection = self.white_coins if name == 'white_coins' else self.black_coins
            for j_coin in arr:
                if j_coin is not None:
                    coin = Coin(j_coin['color'], j_coin['id'], j_coin['type'])
                    coin.set_foreward_vector(j_coin['foreward'])
                    self.set_coin_y_x(coin, j_coin['y'], j_coin['x'])
                    collection[j_coin['id']] = coin

    #todo
    def get_moves_for_coin(self, coin):
        if "coin" == coin.type:
            moves = self.get_obligatory_moves(coin, [])
            if moves:
                coin.moves["obligatory"] = moves
            else:
                coin.moves["normal"] = self.get_no_jump_moves(coin)

    #obligatory means if player can beat coin he must do it
    def get_obligatory_moves(self, coin, move_list, move=None, debug=0):
        if self.have_obligatory_move(coin, move):
            for y, x in itertools.product((1,-1),repeat = 2):
                try:
                    coin_in_direction = self.get_coin_in_direction(coin, (y, x))
                    if self.can_jump_in_direction(coin, coin_in_direction, (y, x), move):
                        next_y, next_x = coin_in_direction.y + y, coin_in_direction.x + x

                        move_inst = {'pos':[], 'beated_coins':[]} if move is None else copy.deepcopy(move)
                        move_inst['pos'].append((next_y, next_x))
                        move_inst['beated_coins'].append(coin_in_direction)

                        coin1 = copy.deepcopy(coin)
                        coin1.y = next_y
                        coin1.x = next_x

                        if move_inst not in move_list\
                        and not self.have_obligatory_move(coin1, move_inst)\
                        and not self.same_pos_in_movelist(move_inst, move_list):
                            move_list.append(move_inst)

                        self.get_obligatory_moves(coin1, move_list, move_inst)
                except BoardError:
                    pass
        return move_list

    def get_no_jump_moves(self, coin):
        move_list = []
        for y,x in [(coin.foreward, 1), (coin.foreward, -1)]:
            try:
                self.get_coin_in_direction(coin, (y, x))
            except NoCoinError:
                move = {"pos":(coin.y + y, coin.x + x)}
                move_list.append(move)
            except OutOfBoardError:
                pass
        return move_list

    def have_obligatory_move(self, coin, move):
        for y, x in [(1,1), (1,-1), (-1, 1), (-1,-1)]:
            try:
                coin_in_direction = self.get_coin_in_direction(coin, (y,x))
                if self.can_jump_in_direction(coin, coin_in_direction, (y,x), move): return True
            except BoardError:
                pass
        return False

    def get_coin_in_direction(self, coin, vector):
        y, x = (coin.y + vector[0], coin.x + vector[1])
        if not self.field_in_board(y, x): raise OutOfBoardError('Field in direction out of the board')
        coin_in_direction = self.fields[y][x].coin
        if coin_in_direction is None: raise NoCoinError('No coin in this direction')
        return coin_in_direction

    def can_jump_in_direction(self, coin, coin_in_direction, vector, move):
        """coins have different colors"""
        if coin_in_direction.color == coin.color: return False
        """field after is in board"""
        y, x = (v*2 for v in vector)
        if not self.field_in_board(coin.y + y, coin.x + x): return False
        """field after jump is either free or coin on that field is not coin who jumps"""
        next_field = self.fields[coin.y + y][coin.x + x]
        if next_field.coin is not None\
        and not self.same_coin(coin, next_field.coin): return False
        """if move is calculating and coin_in_direction wasn't beated yet"""
        if move is not None and self.same_coin_in(coin_in_direction, move['beated_coins']): return False

        return True

    def field_in_board(self, y, x):
        return y in range(self.board_size) and x in range(self.board_size)

    def same_coin_in(self, coin, array):
        for coin1 in array:
            if self.same_coin(coin, coin1): return True
        return False

    def same_coin(self, coin1, coin2):
        return coin1.id == coin2.id and coin1.color == coin2.color

    def same_pos_in_movelist(self, move, move_list):
        for move_l in move_list:
            if set(move_l['pos']) == set(move['pos']): return True
        return False
