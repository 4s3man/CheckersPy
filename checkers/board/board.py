from checkers.board.pawn import *
from checkers.board.state import *

class Board():
    board_size = 8
    pawns_for_site = 12
    def __init__(self, state: State = InitialState()):
        self.white_pawns = state.white_pawns
        self.black_pawns = state.black_pawns
        self.fields = [[None for x in range(self.board_size)] for y in range(self.board_size)]
        for pawn in self.black_pawns:
            self.fields[pawn.y][pawn.x] = self.black_pawns[pawn.id]
        for pawn in self.white_pawns:
            self.fields[pawn.y][pawn.x] = self.white_pawns[pawn.id]
