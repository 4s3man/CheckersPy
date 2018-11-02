from checkers.board.pawn import *
from checkers.board.state import *

class Board():
    board_size = 8
    pawns_for_site = 12
    state = None
    def __init__(self, state: State = InitialState()):
        self.state = state
        self.fields = [[None for x in range(self.board_size)] for y in range(self.board_size)]
        for pawn in state.black_pawns:
            self.place_pawn(pawn)
        for pawn in state.white_pawns:
            self.place_pawn(pawn)

    def place_pawn(self, pawn):
        try:
            collection = self.state.white_pawns if pawn.color == 'white' else self.state.black_pawns
            self.fields[pawn.y][pawn.x] = collection[pawn.id]
        except AttributeError:
            pass
