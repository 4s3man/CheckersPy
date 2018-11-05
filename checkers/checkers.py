from checkers.board.board import *

class Checkers():
    state = None
    move_resolver = None
    max_min = None

    def __init__(self, state: State):
        self.move_resolver = MoveResolver()

        self.state = self.move_resolver.resolve_moves(state)
