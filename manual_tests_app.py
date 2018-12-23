from flask import Flask, render_template, request, session
import time
from checkers.checkers import *
from helpers.connection import *

from checkers.tests.fixtures.state_fixtures import *
from manual_tests.modules import *

state = no_moves_for_black()
# state = initial_state()

checkers = Checkers(state)
checkers.resolve_moves('white')


session['board_state'] = checkers.state.json_encode()
session['turn'] = 'white'
print(session['board_state'])
