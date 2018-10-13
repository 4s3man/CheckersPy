from pprint import pprint

from flask import Flask, render_template
app = Flask(__name__)

class Coin:
    type='coin'
    def __init__(self, color, id):
        self.color = color
        self.id = color + '_' + str(id)
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def html(self):
        return '<span id="%s" class="%s coin--%s"></span>' % (self.id, self.type, self.color)

class BoardField:
    coin = 0
    def set_coin(self, coin, x, y):
        self.coin = coin
        self.coin.x = x
        self.coin.y = y

    def unset_coin(self):
        self.coin = 0

    def get_html(self):
        return '' if not self.coin else\
        self.coin.html()

class Board:
    def __init__(self):
        self.white_coins = [Coin('white', x) for x in range(8)]
        self.black_coins = [Coin('black', x) for x in range(8)]
        self.fields = [[BoardField() for x  in range(8)] for y in range(8)]
    def set_initial_state(self):
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

@app.route('/', methods=['POST', 'GET'])
def checkers():
    board = Board()
    board.set_initial_state()
    return render_template('checkers.html', board = board.fields)

        # if self.coin == 'white' return '<span class="coin coin-white"></span>'
        # else if self.coin == 'white'

    # def set_coin_white(self):
    #     self.coin = 1
    # def unset_coin(self):
    #     self.coin = 0
    #
    # def get_field_html(self):
    #     return coin ? '<span'
