from flask import Flask, render_template, request, session
import json
import itertools
app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

class BoardError(Exception):
    pass

class NoCoinError(BoardError):
    pass

# class SameCoinIdErrror(Exception):
#     pass

class Move:
    """Colection of fields in visiting order field = (position_y, position_x)"""
    visited_fields_yx = []
    """Colection of beated coins coin = <Object Coin>"""
    beated_coins = []


class Coin:
    id = 0
    color = ''
    foreward = 0
    type = ''
    moves = []
    y = 0
    x = 0
    def __init__(self, color, id, type='coin'):
        self.color = color
        self.id = id
        self.type = type

    def set_foreward_vector(self, vector):
        self.foreward = vector

    def html(self):
        return '<span id="%s" class="%s coin--%s"></span>' % (
            self.color + str(self.id), self.type, self.color)


class BoardField:
    coin = None
    def set_coin(self, coin, y, x):
        self.coin = coin
        self.coin.y = y
        self.coin.x = x

    def unset_coin(self):
        self.coin = None

    def get_html(self):
        return '' if not self.coin else\
            self.coin.html()

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
    def get_available_moves(self, color):
        print(color)
    #todo
    def get_moves_for_coin(self, coin, move = None, recurence_counter = 0):
        if "coin" == coin.type:
            moves = self.get_obligatory_moves(coin, [])
            # print('moves amount: ', len(moves))
            # for move in moves:
            #     print('fields: ', move.visited_fields_yx)
            #     print('beated_coins_id: ', [coin.id for coin in move.beated_coins])

    #obligatory means if player can beat coin he must do it
    def get_obligatory_moves(self, coin, move_list, move=None, debug=0):
        if self.have_obligatory_move(coin, move):
            print('ok')


        #     print('ok')
        #     if move not in move_list:
        #         move_list.append(move)
        #         move = None
        # if self.have_obligatory_move(coin, move):
        # for direction_yx in itertools.product((1,-1),repeat = 2):
        #     try:
        #         coin_in_direction = self.get_coin_in_direction(coin, direction_yx)
        #         if self.can_jump_in_direction(coin, coin_in_direction, direction_yx, move):
        #             after_jump_y, after_jump_x = coin_in_direction.y + direction_yx[0], coin_in_direction.x + direction_yx[1]
        #
        #             if move is None: move = Move()
        #             move.beated_coins.append(coin_in_direction)
        #             move.visited_fields_yx.append((after_jump_y, after_jump_x))
        #
        #             coin_after_jump = coin
        #             coin_after_jump.y = after_jump_y
        #             coin_after_jump.x = after_jump_x
        #
        #             if self.have_obligatory_move(coin_after_jump, move):
        #                 self.get_obligatory_moves(coin_after_jump, move_list, move, debug+1)
        #             else:
        #                 move_list.append(move)
        #                 move = None
        #                 return
        #     except BoardError:
        #         pass
        # return move_list

    def have_obligatory_move(self, coin, move):
        for y, x in [(1,1), (1,-1), (-1, 1), (-1,-1)]:
            try:
                coin_in_direction = self.get_coin_in_direction(coin, (y,x))
                return self.can_jump_in_direction(coin, coin_in_direction, (y,x), move)
            except BoardError:
                pass
        return False

    def get_coin_in_direction(self, coin, vector):
        y, x = (coin.y + vector[0], coin.x + vector[1])
        coin_in_direction = self.fields[y][x].coin
        if not self.field_in_board(y, x): raise BoardError('Field in direction out of the board')
        if coin_in_direction is None: raise NoCoinError('No coin in this direction')
        #if encounters itself
        if coin.color == coin_in_direction.color and coin.id == coin_in_direction.id: raise NoCoinError('Same coin in direction')
        return coin_in_direction

    def can_jump_in_direction(self, coin, coin_in_direction, vector, move):

        #coins have different colors
        if coin_in_direction.color == coin.color: return False

        #field after is in board
        y, x = (v*2 for v in vector)
        if not self.field_in_board(coin.y + y, coin.x + x): return False

        #field after jump is free
        if self.fields[coin.y + y][coin.x + x].coin is not None: return False

        #if move is calculating and coin_in_direction wasn't beated yet
        if move is not None and coin_in_direction in move.beated_coins: return False

        return True

    def field_in_board(self, y, x):
        return y in range(self.board_size) and x in range(self.board_size)

"""Remove"""
def recTest():
    print('ok')
"""Remove"""

@app.route('/', methods=['POST', 'GET'])
def checkers():
    board = Board()
    # board.set_initial_state()
    json = board.json_encode_coins()


    # board.set_coin_y_x(Coin('black', 1), 2, 2)
    # board.set_coin_y_x(Coin('white', 2), 1, 1)
    # board.set_coin_y_x(Coin('white', 2), 3, 1)
    # board.set_coin_y_x(Coin('white', 3), 3, 3)
    # board.set_coin_y_x(Coin('white', 4), 5, 3)
    # board.set_coin_y_x(Coin('white', 1), 3, 1)
    # board.get_moves_for_coin(board.fields[2][0].coin)

    # if 'coins' not in session:
    #     session['coins'] = board.json_encode_coins()
    # else:
    #     board.set_coins_from_json(session['coins'])
    return render_template('checkers.html', board=board.fields)

# @app.route('/ajax/move', methods=['POST'])
# def move():
#     return 'ok'
