from flask import Flask, render_template, request, session
from modules import Board as b
import time
# from checkers.board import board as cb
from checkers.checkers import *

app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'


@app.route('/', methods=['POST', 'GET'])
def checkers():
    state = State()
    state.white_pawns[1] = Pawn('white', 2)
    state.white_pawns[1].set_positon(1,1)
    state.white_pawns[1].set_foreward_vector(1)
    state.white_pawns[1].moves = {'beated_coin_ids':[1,2,3,4], "fields": [(1,2), (3,4)]}

    checkers = Checkers(state)
    print(checkers.state.white_pawns[1].moves)
    session['board_state'] = checkers.state.json_encode()

    # if not 'board_state' in session.keys():
    #     checkers = Checkers(InitialState())
    #     session['board_state'] = checkers.state.json_encode()

    return render_template('empty.html')


@app.route('/move', methods=['POST'])
def move():
    # time.sleep(2)
    return session['board_state']
