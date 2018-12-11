def import_all():
    from flask import Flask, render_template, request, session
    import time
    from checkers.checkers import *
    from helpers.connection import *

    from checkers.tests.fixtures.state_fixtures import *
    from manual_tests.modules import *


def print_state_assertion(state:State):
    # print(checkers.state.black_pawns[1].moves)
    for pawn in state.white_pawns + state.black_pawns:
        if pawn:
            # print(pawn.id, pawn.moves, '\n')
            collection = 'black_pawns' if pawn.color == 'black' else 'white_pawns'
            print("assert", pawn.moves, '\\')
            print("==state."+collection+"[" + str(pawn.id) + "].moves", "\n")
