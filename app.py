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

    # state = one_coin_at_1_1()
    state = different_coins_around_white()

    checkers = Checkers(state)
    session['board_state'] = checkers.state.json_encode()

    # if not 'board_state' in session.keys():
    #     checkers = Checkers(InitialState())
    #     session['board_state'] = checkers.state.json_encode()

    return render_template('empty.html')


@app.route('/move', methods=['POST'])
def move():
    # time.sleep(2)
    return session['board_state']
