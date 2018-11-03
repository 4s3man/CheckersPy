from flask import Flask, render_template, request, session
from modules import Board as b
import time
from checkers.board import board as cb

app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'


@app.route('/', methods=['POST', 'GET'])
def checkers():
    state = cb.State()
    state.white_pawns[1] = cb.Pawn('white', 2)
    state.white_pawns[1].set_positon((1,1))
    state.white_pawns[1].set_foreward_vector(1)
    state.white_pawns[1].moves = {'beated_coin_ids':[1,2,3,4], "fields": [(1,2), (3,4)]}

    board = cb.Board(state)

    # state.json_decode(board.state.json_encode())

    # print(state.white_pawns[1].__dict__)
    session['board_state'] = state.json_encode()

    # print(session['board_state'])
    board1 = cb.Board(cb.State(session['board_state']))
    print(board1.state.__dict__)
    # state.json_decode(session['board_state'])

    return render_template('empty.html')

@app.route('/move', methods=['POST'])
def move():
    # time.sleep(2)
    return session['board_state']
