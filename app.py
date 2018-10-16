from flask import Flask, render_template, request, session
import json
import itertools
app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

class InvalidOperationError(Exception):
    pass

class Coin:
    def __init__(self, color, id, type='coin'):
        self.color = color
        self.id = str(id)
        self.type = type

    def set_foreward_vector(self, vector):
        self.foreward = vector

    def html(self):
        return '<span id="%s" class="%s coin--%s"></span>' % (
            self.color + self.id, self.type, self.color)


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
# todo jak to wrzucic do obiektu board najlepiej
def obj_dict(obj):
    return obj.__dict__


class Board:
    def __init__(self):
        self.fields = [[BoardField() for x in range(8)] for y in range(8)]
        self.white_coins = []
        self.black_coins = []

    def set_coin_y_x(self, coin, y, x):
        if y in range(8) and x in range(8):
            self.fields[y][x].set_coin(coin, y, x)
        else:
            raise InvalidOperationError("Invalid operation")

    def unset_coin(self, coin):
        self.fields[coin.y][coin.x].unset_coin()

    def set_initial_state(self):
        self.white_coins = [Coin('white', id) for id in range(8)]
        self.black_coins = [Coin('black', id) for id in range(8)]
        for i, coin in enumerate(self.white_coins):
            if not i % 2:
                self.set_coin_y_x(coin, 6, i)
            else:
                self.set_coin_y_x(coin, 7, i)
                self.set_coin_y_x(coin, 5, i)
            coin.set_foreward_vector(-1)
        for i, coin in enumerate(self.black_coins):
            if not i % 2:
                self.set_coin_y_x(coin, 0, i)
                self.set_coin_y_x(coin, 2, i)
            else:
                self.set_coin_y_x(coin, 1, i)
            coin.set_foreward_vector(1)

    def json_encode_coins(self):
        coins = {
            'white_coins': self.white_coins,
            'black_coins': self.black_coins}
        return json.dumps(coins, default=obj_dict)

        #przetestować bo po dodaniu coin.foreward powinno być zepsute
    def set_coins_from_json(self, json_coins):
        coins = json.loads(json_coins)
        for name, arr in coins.items():
            collection = self.white_coins if name == 'white_coins' else self.black_coins
            for j_coin in arr:
                coin = Coin(j_coin['color'], j_coin['id'])
                self.fields[j_coin['y']][j_coin['x']].set_coin(
                    coin, j_coin['y'], j_coin['x'])
                collection.append(coin)
    #todo
    def get_available_moves(self, color):
        print(color)
    #todo
    def get_moves_for_coin(self, coin, moves = [], recurence_counter = 0):
        if "coin" == coin.type:
            vectors = itertools.product((1,-1),repeat = 2)
            for yx in vectors:
                if self.enemy_in_this_direction(coin, yx):
                    print(coin.foreward)

    def enemy_in_this_direction(self, coin, vector):
        y, x = vector
        if coin.y + y not in range(8) or coin.x + x not in range(8): return False
        destination_field = self.fields[coin.y + vector[0]][coin.x + vector[1]]
        return destination_field.coin is not None and destination_field.coin.color != coin.color

    def can_jump_in_direction(self, coin, vector):
        y, x = (v*2 for v in vector)
        if coin.y + y not in range(8) or coin.x + x not in range(8): return False
        return self.fields[coin.y + y][coin.x + x].coin is None
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
    # board.set_initial_state()
    # board.get_moves_for_coin(board.fields[0][0].coin)
    # if 'coins' not in session:
    #     session['coins'] = board.json_encode_coins()
    # else:
    #     board.set_coins_from_json(session['coins'])
    return render_template('checkers.html', board=board.fields)

# @app.route('/ajax/move', methods=['POST'])
# def move():
#     return 'ok'
