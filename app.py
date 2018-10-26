from flask import Flask, render_template, request, session
from modules import Board as b

app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'


@app.route('/', methods=['POST', 'GET'])
def checkers():
    board = b.Board()
    # board.set_initial_state()
    json = board.json_encode_coins()
    black_coins = [b.Coin('white', i) for i in range(5)]
    coin = b.Coin('black', 2)
    coin.set_foreward_vector(-1)
    board.set_coin_y_x(coin, 5, 1)
    board.set_coin_y_x(black_coins[0], 4, 2)
    board.set_coin_y_x(black_coins[1], 2, 4)
    board.set_coin_y_x(black_coins[2], 4, 0)
    board.set_coin_y_x(black_coins[3], 4, 2)
    # board.set_coin_y_x(black_coins[4], 6, 4)

    # move = {'beated_coins':[black_coins[1]]}

    print('hoave bligaory: ',board.have_obligatory_move(coin, None))
    board.get_moves_for_coin(coin)
    print(coin.moves)


    # for move in moves:
    #     dono = 'pos: ' + str(move['pos']) + ' coins: ' + str([(coin.x, coin.y) for coin in move['beated_coins']])
    #     print(dono)
    # board.set_coin_y_x(coin, 5, 5)
    # print(board.have_obligatory_move(coin, None))


    # if 'coins' not in session:
    #     session['coins'] = board.json_encode_coins()
    # else:
    #     board.set_coins_from_json(session['coins'])
    return render_template('checkers.html', board=board.fields)

# @app.route('/ajax/move', methods=['POST'])
# def move():
#     return 'ok'
