from flask import Flask, render_template, request, session
import json
import itertools
app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

class BoardError(Exception):
    pass

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
        else:
            raise BoardError("Wanted to set coin out of the board")

    def unset_coin(self, coin):
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
            for direction_yx in itertools.product((1,-1),repeat = 2):
                try:
                    coin_in_direction = self.get_coin_in_direction(coin, direction_yx)
                    if coin_in_direction is not None:
                        if self.can_jump_in_direction(coin, coin_in_direction, direction_yx, move):
                            print('ok')
                            # move = Move() if move is None
                            # move.beated_coins.append(coin_in_direction)
                            # move.visited_fields_yx.append(coin_in_direction.y + direction_yx[0], coin_in_direction.x + direction_yx[1])
                except BoardError:
                    pass

    def get_coin_in_direction(self, coin, vector):
        y, x = (coin.y + vector[0], coin.x + vector[1])
        if self.field_in_board(y, x):
            if self.fields[y][x].coin is not coin:
                return self.fields[y][x].coin
        else:
            raise BoardError('Field in direction out of the board')

    # def enemy_in_this_direction(self, coin, vector):
    #     y, x = vector
    #     if coin.y + y not in range(self.board_size) or coin.x + x not in range(self.board_size): return False
    #     destination_field = self.fields[coin.y + vector[0]][coin.x + vector[1]]
    #     return destination_field.coin is not None and destination_field.coin.color != coin.color

    def can_jump_in_direction(self, coin, coin_in_direction, vector, move):

        #coins have different colors
        if coin_in_direction.color == coin.color: return False

        #field after is in board
        y, x = (v*2 for v in vector)
        if not self.field_in_board(y, x): return False

        #field after jump is free
        if self.fields[coin.y + y][coin.x + x].coin is not None: return False

        #if move is calculating and coin_in_direction wasn't beated yet
        if move is not None and coin_in_direction in move.beated_coins: return False

        return True

    def field_in_board(self, y, x):
        return y in range(self.board_size) and x in range(self.board_size)
    # def get_fields_around(self, coin):
    #     vectors = itertools.product((1,-1),repeat = 2)
    #     fields_around = []
    #     for yx in vectors:
    #         field_y = coin.y + yx[0]
    #         field_x = coin.x + yx[1]
    #         if field_y in range(8) and field_x in range(8):
    #             fields_around.append(self.fields[field_y][field_x])
    #     return fields_around
        # return [ self.fields[coin.y + yx[0]][coin.x + yx[1]] for yx in vectors if coin.x and coin.y in range(1, 6)]
    # def move_coin(self, coin, pos):
    #     #check if there would be no other coins if coin can move there
    #     if pos in coin.moves():
    #         y, x = pos
    #         #check if on wanted field is another coin
    #         if self.fields[y][x].coin != 0:
    #             #todo move when encounter another coin
    #             print('no ok')
    #         else:
    #             self.fields[coin.y][coin.x].unset_coin()
    #             self.fields[y][x].set_coin(coin, y, x)


@app.route('/', methods=['POST', 'GET'])
def checkers():
    board = Board()
    board.set_initial_state()
    json = board.json_encode_coins()

    # board.set_coin_y_x(Coin('white', 12), 3, 1)
    # board.get_moves_for_coin(board.fields[2][0].coin)
    a = [Coin('white', 1)]
    b = a
    print(a[0] is b[0])


    # if 'coins' not in session:
    #     session['coins'] = board.json_encode_coins()
    # else:
    #     board.set_coins_from_json(session['coins'])
    return render_template('checkers.html', board=board.fields)

# @app.route('/ajax/move', methods=['POST'])
# def move():
#     return 'ok'
