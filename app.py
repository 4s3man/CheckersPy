from flask import Flask, render_template, request, session
from modules import Board as b
from checkers.board import board as cb

app = Flask(__name__)

app.secret_key = '$$_asdoi20z1|}2!{_012!!_\z!@669xcz^[%mmaq'


@app.route('/', methods=['POST', 'GET'])
def checkers():

    board = cb.Board()

    session['board_state'] = board.state.json_encode()
    return render_template('empty.html')

@app.route('/move', methods=['POST'])
def move():
    return session['board_state']
