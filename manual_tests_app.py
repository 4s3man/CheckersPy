from flask import Flask, render_template, request, session
import time
from checkers.checkers import *
from helpers.connection import *

from checkers.tests.fixtures.state_fixtures import *
from manual_tests.modules import *

# state = no_blocked_beating_move_bug()
state = only_queens_state()

checkers = Checkers(state)
checkers.resolve_moves('white')


print(has_only_queens(checkers.state))

session['board_state'] = checkers.state.json_encode()
session['turn'] = 'white'
