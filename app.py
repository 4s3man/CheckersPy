from flask import Flask, render_template, request, session
import time
from checkers.checkers import *
from helpers.connection import *

app = Flask(__name__)
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

@app.route('/', methods=['POST', 'GET'])
def checkers():

    """For local Development"""
    import manual_tests_app

    # if not 'board_state' in session.keys():
    #     checkers = Checkers(InitialState())
    #     checkers.resolve_moves('white')
    #     session['board_state'] = checkers.state.json_encode()
    #     session['turn'] = 'white'

    return render_template('empty.html')

@app.route('/move', methods=['POST'])
def move():
    # print(request.get_json())
    try:
        pawn_move = receive_pawn_move(request.get_json(), session['turn'])
        checkers = Checkers(State(session['board_state']))
        if not checkers.pawn_move_is_valid(**pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')

        lost_pawns = [None for x in range(13)]
        if checkers.state.white_pawns == lost_pawns or checkers.state.black_pawns == lost_pawns: return {'winner':session[turn]}
        session['turn'] = 'white' if session['turn'] == 'black' else 'black'

        checkers.make_move(**pawn_move)
        checkers.resolve_moves(session['turn'])
        # print(checkers.state.json_encode())


        session['board_state'] = checkers.state.json_encode()
    except EmptyPawnMove:
        # print('EmptyPawnMove')
        pass
    except InvalidPawnMove:
        """Handle some error"""
        # print('invalidPawnMove Error')
    # print('ok')
    # time.sleep(2)
    return strip_redundant_for_frontend(session['board_state'])
