from flask import Flask, render_template, request, session, url_for, redirect
# from flask_socketio import SocketIO, join_room, emit, rooms
import time
from secrets import token_urlsafe
from checkers.checkers import *
from helpers.connection import *

app = Flask(__name__)
# socketio = SocketIO(app)
ROOMS = {}
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

@app.route('/', methods=['GET', 'POST'])
def choose_game():
    return render_template('choose_game.html')

# @socketio.on('create')
# def on_create(data):
#     room = 2
#     ROOMS[room] = 'dono'
#     join_room(room)
#     emit('join_room', {'room':room})
#     print('dziala\n\n\n\n\n\n\n')
#     print(rooms())



@app.route('/game', methods=['POST', 'GET'])
def checkers():
    hot_seat_token = token_urlsafe(22)
    session['hot_seat_token'] = hot_seat_token

    # """For local Development"""
    # import manual_tests_app

    if not 'board_state' in session.keys():
        checkers = Checkers(InitialState())
        checkers.resolve_moves('white')
        session['board_state'] = checkers.state.json_encode()
        session['turn'] = 'white'
        session['draw_count'] = 0

    return render_template('game.jinja2')

@app.route('/game_controller', methods=['POST'])
def game_controller():
    print(request.get_json())
    # print('\n\n\n\n\n\n',request.form)
    # if request.form.get('leave_token', '') == session.get('hot_seat_token', 'no'):
    #     del session['turn']
    #     del session['draw_count']
    #     del session['board_state']
    #     del session['hot_seat_token']
    #     return redirect(url_for('choose_game'))
    # elif request.form.get('reset_token', '') == session.get('hot_seat_token', 'no'):
    #     checkers = Checkers(InitialState())
    #     checkers.resolve_moves('white')
    #     session['board_state'] = checkers.state.json_encode()
    #     session['turn'] = 'white'
    #     session['draw_count'] = 0
    #     return redirect(url_for('choose_game'))
    # if request.form.get('redirect', '') == 'checkers':
    #
    #     return redirect(url_for('checkers'))

    return 'game_controller'

@app.route('/move', methods=['POST'])
def move():
    # print(request.get_json())

    try:
        pawn_move = receive_pawn_move(request.get_json(), session['turn'])
        checkers = Checkers(State(session['board_state']))
        if not checkers.pawn_move_is_valid(**pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')

        checkers.make_move(**pawn_move)

        checkers.state.winner = checkers.state.get_winner()
        if has_only_queens(checkers.state) and not checkers.state.winner:
            session['draw_count'] += 1
            if(session['draw_count'] > 6):
                checkers.state.winner = 'draw'

        session['turn'] = 'white' if session['turn'] == 'black' else 'black'
        checkers.resolve_moves(session['turn'])

        session['board_state'] = checkers.state.json_encode()
        # print(session['board_state'] )
    except EmptyPawnMove:
        print('EmptyPawnMove')
        pass
    except InvalidPawnMove:
        """Handle some error"""
        # print('invalidPawnMove Error')
    # print('ok')
    # time.sleep(2)
    return strip_redundant_for_frontend(session['board_state'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # socketio.run(app, debug=True)
   # app.run(host="0.0.0.0", port=5009, debug=True)
