from flask import Flask, render_template, request, session
import json
app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

class Coin:
    def __init__(self, color, id, type = 'coin'):
        self.color = color
        self.id = str(id)
        self.type = type

    def html(self):
        return '<span id="%s" class="%s coin--%s"></span>' % (self.color + self.id, self.type, self.color)

    def moves(self):
        moves = []
        if self.type == 'coin':
            if self.color == 'white':
                if self.x-1 >= 0: moves.append((self.y+1, self.x-1))
                if self.x+1 <= 7: moves.append((self.y+1, self.x+1))
            else:
                if self.x-1 >= 0: moves.append((self.y-1, self.x-1))
                if self.x+1 <= 7: moves.append((self.y-1, self.x+1))
        return moves

class BoardField:
    coin = 0
    def set_coin(self, coin, y, x):
        self.coin = coin
        self.coin.y = y
        self.coin.x = x

    def unset_coin(self):
        self.coin = 0

    def get_html(self):
        return '' if not self.coin else\
        self.coin.html()
#todo jak to wrzucic do obiektu board najlepiej
def obj_dict(obj):
    return obj.__dict__

class Board:

    def __init__(self):
        self.fields = [[BoardField() for x  in range(8)] for y in range(8)]
        self.white_coins = []
        self.black_coins = []

    def set_initial_state(self):
        self.white_coins = [Coin('white', id) for id in range(8)]
        self.black_coins = [Coin('black', id) for id in range(8)]
        for i, coin in enumerate(self.white_coins):
            if not i%2:
                self.fields[0][i].set_coin(coin, 0, i)
            else:
                self.fields[1][i].set_coin(coin, 1, i)
        for i, coin in enumerate(self.black_coins):
            if not i%2:
                self.fields[6][i].set_coin(coin, 6, i)
            else:
                self.fields[7][i].set_coin(coin, 7, i)

    def json_encode_coins(self):
        coins = {'white_coins':self.white_coins, 'black_coins':self.black_coins}
        return json.dumps(coins, default=obj_dict)

    def set_coins_from_json(self, json_coins):
        coins = json.loads(json_coins)
        for name, arr in coins.items():
            collection = self.white_coins if name == 'white_coins' else self.black_coins
            for j_coin in arr:
                coin = Coin(j_coin['color'], j_coin['id'])
                self.fields[j_coin['y']][j_coin['x']].set_coin(coin, j_coin['y'], j_coin['x'])
                collection.append(coin)

    def move(self, coin, pos):
        #check if there would be no other coins if coin can move there
        if pos in coin.moves():
            y, x = pos
            #check if on wanted field is another coin
            if self.fields[y][x].coin != 0:
                #todo move when encounter another coin
                print('no ok')
            else:
                self.fields[coin.y][coin.x].unset_coin()
                self.fields[y][x].set_coin(coin, y, x)

@app.route('/', methods=['POST', 'GET'])
def checkers():
    board = Board()
    board.set_initial_state()
    if not 'coins' in session:
        session['coins'] = board.json_encode_coins()
    else:
        board.set_coins_from_json(session['coins'])
    return render_template('checkers.html', board = board.fields)

# @app.route('/ajax/move', methods=['POST'])
# def move():
#     return 'ok'
