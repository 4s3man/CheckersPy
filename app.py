from flask import Flask, render_template, request, session
import time
from checkers.checkers import *
from helpers.connection import *

"""For debug testing purposes"""
from checkers.tests.fixtures.state_fixtures import *
"""For debug testing purposes end"""

app = Flask(__name__)
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

@app.route('/', methods=['POST', 'GET'])
def checkers():

    """For making tests"""
    state = for_queen_blocking_pawns_state()

    checkers = Checkers(state)
    checkers.resolve_moves('white')
    # for pawn in state.white_pawns + state.black_pawns:
    #     if pawn:
    #         # print(pawn.id, pawn.moves, '\n')
    #         collection = 'black_pawns' if pawn.color == 'black' else 'white_pawns'
    #         print("assert", pawn.moves, '\\')
    #         print("==state."+collection+"[" + str(pawn.id) + "].moves", "\n")
    """For making tests end"""

    # test_pawn_move = {'id': 3, 'color': 'white', 'move': {'position_after_move': [4, 6]}}
    # print(checkers.pawn_move_is_valid(**test_pawn_move))
    # print(make_move(checkers.state, **test_pawn_move).white_pawns[3].__dict__)


    # try:
    #     pawn_move = receive_pawn_move(test_pawn_move)
    #     checkers2 = Checkers(State(session['board_state']))
    #     if not checkers.pawn_move_is_valid(**pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')
    #     checkers.make_move(**pawn_move)
    # except EmptyPawnMove:
    #     print('EmptyPawnMove')
    #     pass
    # except InvalidPawnMove:
    #     """Handle some error"""
    #     print('invalidPawnMove Error')
    session['board_state'] = checkers.state.json_encode()


    # if not 'board_state' in session.keys():
    #     checkers = Checkers(InitialState())
    #     checkers.resolve_moves('white')
    #     session['board_state'] = checkers.state.json_encode()
    #     session['turn'] = 'white'

    return render_template('empty.html')

@app.route('/move', methods=['POST'])
def move():
    try:
        pawn_move = receive_pawn_move(request.get_json())
        checkers = Checkers(State(session['board_state']))
        if not checkers.pawn_move_is_valid(**pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')
        checkers.make_move(**pawn_move)
        checkers.resolve_moves('white')
        session['board_state'] = checkers.state.json_encode()
    except EmptyPawnMove:
        print('EmptyPawnMove')
        pass
    except InvalidPawnMove:
        """Handle some error"""
        print('invalidPawnMove Error')
    # print('ok')
    # time.sleep(2)
    return session['board_state']
