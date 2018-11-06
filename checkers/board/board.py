from checkers.board.state import *
from checkers.board.errors import *

class Board():
    board_size = 8
    pawns_for_site = 12
    fields = [[]]

    def __init__(self, state: State = None):
        if state:
            self.place_pawns(state)

    def place_pawns(self, state: State):
        self.fields = [[None for x in range(self.board_size)] for y in range(self.board_size)]

        self.place_pawns_from_collection(state.white_pawns)
        self.place_pawns_from_collection(state.black_pawns)

    def place_pawns_from_collection(self, collection: list):
        try:
            for pawn in collection:
                if self.has_position(pawn.y, pawn.x):
                    self.fields[pawn.y][pawn.x] = collection[pawn.id]
        except AttributeError:
            pass

    def has_position(self, y:int, x:int):
        return y in range(self.board_size) and x in range(self.board_size)
