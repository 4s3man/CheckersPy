from flask import Flask, render_template, request, session, url_for, redirect
# from flask_socketio import SocketIO, join_room, emit, rooms
import time
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

@app.route('/game/hotseat', methods=['POST', 'GET'])
def hot_seat():
    # """For local Development"""
    # import manual_tests_app

    if not 'board_state' in session.keys():
        checkers = Checkers(InitialState())
        checkers.resolve_moves('white')
        session['board_state'] = checkers.state.json_encode()
        session['turn'] = 'white'
        session['draw_count'] = 0

    return render_template('games/hot_seat.jinja2')

@app.route('/game_controller', methods=['POST'])
def game_controller():
    if request.method == 'POST':
        cmd = request.get_json()
        if cmd == 'reset_hot_seat':
            del_game_sessions()
            set_initial_game_sessions()

            return 'ok'
        elif cmd == 'leave_hot_seat':
            del_game_sessions()
            return url_for('choose_game')

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
        # print('EmptyPawnMove')
        pass
    except InvalidPawnMove:
        """Handle some error"""
        # print('invalidPawnMove Error')
    except KeyError:
        set_initial_game_sessions()
        print('key error reseting game')
    # print('ok')
    # time.sleep(2)
    return strip_redundant_for_frontend(session['board_state'])

@app.route('/leave', methods=['GET'])
def leave():
    del_game_sessions()
    return redirect(url_for('choose_game'))

def set_initial_game_sessions():
    checkers = Checkers(InitialState())
    checkers.resolve_moves('white')
    session['board_state'] = checkers.state.json_encode()
    session['turn'] = 'white'
    session['draw_count'] = 0

def del_game_sessions():
    session_keys = session.keys()
    for key in ['turn', 'draw_count', 'board_state']:
        if key in session_keys: del session[key]
    set_initial_game_sessions()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # socketio.run(app, debug=True)
   # app.run(host="0.0.0.0", port=5009, debug=True)
