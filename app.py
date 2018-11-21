from flask import Flask, render_template, request, session
from modules import Board as b
import time
from checkers.checkers import *
from checkers.move_exceptions import *

"""For debug testing purposes"""
from checkers.tests.fixtures.state_fixtures import *
"""For debug testing purposes end"""

app = Flask(__name__)
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

@app.route('/', methods=['POST', 'GET'])
def checkers():

    """For making tests"""
    # state = queen_extended_circle_state()
    #
    # checkers = Checkers(state)
    # for pawn in state.white_pawns + state.black_pawns:
    #     if pawn:
    #         # print(pawn.id, pawn.moves, '\n')
    #         collection = 'black_pawns' if pawn.color == 'black' else 'white_pawns'
    #         print("assert", pawn.moves, '\\')
    #         print("==state."+collection+"[" + str(pawn.id) + "].moves", "\n")
    """For making tests end"""

    test_pawn_move = {'moveData':{'pawn': {'foreward': -1, 'type': 'normal', 'color': 'white', 'id': 2}, 'move': {'position_after_move': [4, 6]}}}

    try:
        pawn_move = receive_pawn_move(test_pawn_move)
        checkers2 = Checkers(State(session['board_state']))
        if not checkers2.pawn_move_is_valid(pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')
        print('ok')
    except EmptyPawnMove:
        print('EmptyPawnMove')
        pass
    except InvalidPawnMove:
        """Handle some error"""
        print('invalidPawnMove Error')


    if not 'board_state' in session.keys():
        checkers = Checkers(InitialState())
        checkers.resolve_moves('white')
        session['board_state'] = checkers.state.json_encode()
        session['turn'] = 'white'

    return render_template('empty.html')

@app.route('/move', methods=['POST'])
def move():
    # try:
    #     pawn_move = receive_pawn_move(request.get_json())
    #     checkers = Checkers(State(session['board_state']))
    # except EmptyPawnMove:
    #     print('empty move')
    #     pass
    # except InvalidPawnMove:
    #     """Handle some error"""
    #     print('invalidPawnMove Error')
    #     return session['board_state']
    #
    # print('ok')
    # time.sleep(2)
    return session['board_state']

"""
Throws:
EmptyPawnMove
InvalidPawnMove exceptions
"""
def receive_pawn_move(posted_data: dict):
    if(not len(posted_data)):raise EmptyPawnMove('Move is empty')
    if(type(posted_data) is dict):
        try:
            pawn_move = posted_data['moveData']
            assert len(posted_data['moveData']) <3
            assert len(pawn_move['pawn']) < 6
            assert len(pawn_move['move']) < 3
            assert len(pawn_move['move'].get('beated_pawn_ids', [])) < 13
            assert pawn_move['pawn']['id'] in range(12)
            assert pawn_move['pawn']['color'] in ['white', 'black']
            assert pawn_move['move']['position_after_move'][0] in range(8)
            assert pawn_move['move']['position_after_move'][1] in range(8)
            for beated_pawn_id in pawn_move['move'].get('beated_pawn_ids', []):
                assert beated_pawn_id in range(12)
        except (KeyError, AssertionError) as e:
            raise InvalidPawnMove('Posted data does not have required pawn_move data')
        return pawn_move
    raise InvalidPawnMove('Posted data is not dict')
