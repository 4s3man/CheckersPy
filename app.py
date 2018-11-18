from flask import Flask, render_template, request, session
from modules import Board as b
import time
from checkers.checkers import *

"""For debug testing purposes"""
from checkers.tests.fixtures.state_fixtures import *
"""For debug testing purposes end"""

app = Flask(__name__)
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

@app.route('/', methods=['POST', 'GET'])
def checkers():

    """For making tests"""
    # state = for_queen_blocking_pawns_state()
    #
    # checkers = Checkers(state)
    # for pawn in state.white_pawns + state.black_pawns:
    #     if pawn:
    #         # print(pawn.id, pawn.moves, '\n')
    #         collection = 'black_pawns' if pawn.color == 'black' else 'white_pawns'
    #         print("assert", pawn.moves, '\\')
    #         print("==state."+collection+"[" + str(pawn.id) + "].moves", "\n")
    """For making tests end"""

    if not 'board_state' in session.keys():
        checkers = Checkers(InitialState())
        checkers.resolve_moves('white')
        session['board_state'] = checkers.state.json_encode()
        session['turn'] = 'white'

    return render_template('empty.html')


@app.route('/move', methods=['POST'])
def move():
    print(request.get_json())
    # time.sleep(2)
    return session['board_state']
