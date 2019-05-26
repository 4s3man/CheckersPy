import sqlite3
import re
from flask import Flask, flash, render_template, request, session, url_for, redirect, g
from checkers.checkers import *
from helpers.connection import *
from checkers.room_index import *
from checkers.maxmin import *
from uuid import uuid4
from bundles.Connection import Connection
from bundles.User import User
from bundles.Captcha import captcha_is_ok
from bundles.Ranking import Ranking

app = Flask(__name__)
ROOMS = RoomIndex()
app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'

connection = Connection()
connection.init_db(app)

@app.teardown_appcontext
def close_connection(exception):
    connection.maybe_close_db()

@app.route('/', methods=['GET', 'POST'])
def choose_game():
    ROOMS.cultivate()
    if request.method == 'POST':
        if request.form['cmd'] == 'create_room':
            session['pid'] = session.get('pid', uuid4().hex)
            session['rid'] = session.get('rid', uuid4().hex)
            ROOMS[session['rid']] = Room(session['pid'])
        if request.form['cmd'] == 'join_any_room':
            room_id = ROOMS.get_free_room_id()
            if 0 != ROOMS.count_joinable() and room_id:
                if not 'pid' in session.keys():
                    session['pid'] = uuid4().hex
                session['rid'] = room_id
                ROOMS.join_room(room_id, session['pid'])
                checkers = Checkers(InitialState())
                checkers.resolve_moves('white')
                ROOMS[room_id].board_state = checkers.state.json_encode()
            else:
                flash('no rooms to join', 'error')
                return redirect(url_for('choose_game'))

        return redirect(url_for('through_net'))

    return render_template('choose_game.html', rooms_number=str(ROOMS.count_joinable()))

@app.route('/ranking', methods=['GET'])
def ranking():
    ranking = Ranking()
    user_id = session.get('user').get('id') if session.get('user') else None
    user_login = session.get('user').get('login') if session.get('user') else None

    return render_template('ranking.jinja2',
        top_20_vs_computer=ranking.find_top_20_for_game(Ranking.VS_COMPUTER),
        top_20_through_net=ranking.find_top_20_for_game(Ranking.THROUGH_NET),
        user_stats=ranking.find_for_user(user_id),
        user_login=user_login
        )

@app.route('/logout', methods=['GET'])
def logut():
    session['user'] = None
    flash('logged out', 'success')
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = User()
    login = ''
    password = ''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if not captcha_is_ok(request):
            flash('invalid captcha', 'error')
        elif not user.validate(login):
            flash('login must contain only ' + user.getAllowedChars(), 'error')
        elif not user.validate(password):
            flash('password must contain only ' + user.getAllowedChars(), 'error')
        elif not user.login_already_exists(login):
            flash('no such login', 'error')
        else:
            user_dict = user.get_user_dict(login, password)
            if user_dict is not None:
                session['user'] = user_dict
                flash('logged in as ' + session['user']['login'], 'success')
                return redirect('/')
            else:
                flash('invalid password', 'error')

    return render_template('login.jinja2',
                           login=login,
                           password=password
                           )

@app.route('/register', methods=['GET', 'POST'])
def register():
    user = User()
    login = ''
    password = ''

    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if not captcha_is_ok(request):
            flash('invalid captcha', 'error')
        elif user.login_already_exists(login):
            flash('login already in use', 'error')
        elif request.form['password'] != request.form['password_confirm']:
            flash('repeated passowrd is not the same as original', 'error')
        elif not user.validate(login):
            flash('login must contain only ' + user.getAllowedChars(), 'error')
        elif not user.validate(password):
            flash('password must contain only ' + user.getAllowedChars(), 'error')
        elif user.login_already_exists(login):
            flash('login already in use', 'error')
        else:
            user.create(login, password)
            flash('successfully registered', 'success')
            return redirect(url_for('login'))

    return render_template('register.jinja2',
                           login=login,
                           password=password
                           )

@app.route('/history', methods=['GET'])
def checkers_history():
    return render_template('history.jinja2')

@app.route('/fetch_rooms', methods=['POST'])
def fetch_rooms():
    return str(ROOMS.count_joinable())

@app.route('/game/through_net', methods=['POST', 'GET'])
def through_net():
    ROOMS.cultivate()
    return render_template('games/through_net.jinja2')

@app.route('/through_net_connection', methods=['POST'])
def thorugh_net_connection():
    if request.method == 'POST':
        if ROOMS.room_exists(session['rid']):
            room = ROOMS[session['rid']]
            player_id = session['pid']
            if not room.is_winned() and room.is_time_up_for_move(datetime.now()):
                room.win_too_long_unmoved()

            if session.get('pid', None) == room.creator_id and room.is_winned():
                if room.winner == 'white':
                    User.increment_score(session, Ranking.THROUGH_NET, Ranking.WIN)
                if room.winner == 'black':
                    User.increment_score(session, Ranking.THROUGH_NET, Ranking.LOST)

            if session.get('pid', None) != room.creator_id and room.is_winned():
                if room.winner == 'white':
                    User.increment_score(session, Ranking.THROUGH_NET, Ranking.LOST)
                if room.winner == 'black':
                    User.increment_score(session, Ranking.THROUGH_NET, Ranking.WIN)


            return json.dumps({'playerTurn':room.turn == player_id, 'joined':room.joiner_id != '', 'winner': room.winner})
        else:
            return json.dumps({'room_error': url_for('choose_game')})


@app.route('/move_through_net', methods=['POST'])
def move_through_net():
    room = ROOMS[session['rid']]
    player_id = session['pid']
    try:
        pawn_move = receive_pawn_move(request.get_json(), room.get_turn_color())
        checkers = Checkers(State(room.board_state))

        if not checkers.pawn_move_is_valid(**pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')

        checkers.make_move(**pawn_move)

        checkers.state.winner = checkers.state.get_winner()
        if has_only_queens(checkers.state) and not checkers.state.winner:
            room.draw_count += 1
            if(room.draw_count > 6):
                User.increment_score(session, Ranking.THROUGH_NET, Ranking.DRAW)
                checkers.state.winner = 'draw'

        room.change_turn()
        checkers.resolve_moves(room.get_turn_color())

        if not checkers.state.collection_has_moves(room.get_turn_color()):
            winner = room.get_turn_color()
            checkers.state.winner = 'white' if winner == 'black' else 'black'

            if session.get('pid', None) == room.creator_id:
                if winner == 'white':
                    User.increment_score(session, Ranking.THROUGH_NET, Ranking.WIN)
                if winner == 'black':
                    User.increment_score(session, Ranking.THROUGH_NET, Ranking.LOST)

        room.board_state = checkers.state.json_encode()
    except EmptyPawnMove:
        print('EmptyPawnMove')
        pass
    except InvalidPawnMove:
        """Handle some error"""
        print('invalidPawnMove Error')
    return strip_redundant_for_frontend(room.board_state)

@app.route('/game/hotseat', methods=['POST', 'GET'])
def hot_seat():
    if not 'board_state' in session.keys():
        set_initial_game_sessions()

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
        elif cmd == 'reset_vs_computer':
            del_game_sessions('_vs_computer')
            set_initial_game_sessions('_vs_computer')
        elif cmd == 'leave_vs_computer':
            del_game_sessions('_vs_computer')
            return url_for('choose_game')
        elif cmd == 'leave_through_net':
            room = ROOMS[session['rid']]
            winner = 'black' if session['pid'] == room.creator_id else 'white';
            checkers = Checkers(State(room.board_state))
            checkers.state.winner = winner
            ROOMS[session['rid']].board_state = checkers.state.json_encode()
            room.winner = winner
            return url_for('choose_game')
        else:
            return 'unsuported_action'

    return 'unsuported_action'

@app.route('/move', methods=['POST'])
def move():
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

        if not checkers.state.collection_has_moves(session['turn']):
            checkers.state.winner = 'white' if session['turn'] == 'black' else 'black'

        session['board_state'] = checkers.state.json_encode()
    except EmptyPawnMove:
        print('EmptyPawnMove')
        pass
    except InvalidPawnMove:
        """Handle some error"""
        print('invalidPawnMove Error')
    except KeyError:
        set_initial_game_sessions()
        print('key error reseting game')
    return strip_redundant_for_frontend(session['board_state'])

@app.route('/game/vs_computer', methods=['POST', 'GET'])
def vs_computer():
    if not 'board_state_vs_computer' in session.keys():
        set_initial_game_sessions('_vs_computer')

    return render_template('games/vs_computer.jinja2')

@app.route('/move_vs_computer', methods=['POST'])
def move_vs_computer():
    try:
        pawn_move = receive_pawn_move(request.get_json(), session['turn_vs_computer'])
        checkers = Checkers(State(session['board_state_vs_computer']))
        if not checkers.pawn_move_is_valid(**pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')
        checkers.make_move(**pawn_move)

        checkers.state.winner = checkers.state.get_winner()
        if has_only_queens(checkers.state) and not checkers.state.winner:
            session['draw_count_vs_computer'] += 1
            if(session['draw_count_vs_computer'] > 6):
                checkers.state.winner = 'draw'

        computer_color = 'white' if session['turn_vs_computer'] == 'black' else 'black'
        move = pick_computer_move(checkers.state, computer_color)
        if move:
            checkers.make_move(**move)

        checkers.state.winner = checkers.state.get_winner()
        if has_only_queens(checkers.state) and not checkers.state.winner:
            session['draw_count_vs_computer'] += 1
            if(session['draw_count_vs_computer'] > 6):
                checkers.state.winner = 'draw'

        checkers.resolve_moves(session['turn_vs_computer'])

        if not checkers.state.collection_has_moves(session['turn_vs_computer']):
            if session['turn_vs_computer'] == 'black':
                checkers.state.winner = 'white'
            else:
                checkers.state.winner = 'black'

        if checkers.state.winner == 'white':
            User.increment_score(session, Ranking.VS_COMPUTER, Ranking.WIN)
        if checkers.state.winner == 'black':
            User.increment_score(session, Ranking.VS_COMPUTER, Ranking.LOST)
        if checkers.state.winner == 'draw':
            User.increment_score(session, Ranking.VS_COMPUTER, Ranking.DRAW)

        session['board_state_vs_computer'] = checkers.state.json_encode()
    except EmptyPawnMove:
        print('EmptyPawnMove')
        pass
    except InvalidPawnMove as e:
        """Handle some error"""
        print('invalidPawnMove Error')
    except KeyError:
        set_initial_game_sessions('_vs_computer')
        print('key error reseting game')
    return strip_redundant_for_frontend(session['board_state_vs_computer'])

@app.route('/leave', methods=['GET'])
def leave():
    del_game_sessions()
    return redirect(url_for('choose_game'))

def set_initial_game_sessions(sufix:str=''):
    """Empty sufix used for hot_seats"""
    checkers = Checkers(InitialState())
    checkers.resolve_moves('white')
    session['board_state' + sufix] = checkers.state.json_encode()
    session['turn' + sufix] = 'white'
    session['draw_count' + sufix] = 0

def del_game_sessions(sufix:str=''):
    """Empty sufix used for hot_seats"""
    session_keys = session.keys()
    for key in ['turn'+ sufix, 'draw_count'+ sufix, 'board_state'+ sufix]:
        if key in session_keys: del session[key]

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('choose_game'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
