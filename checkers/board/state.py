from checkers.board.pawn import *

class State():
    board_size = 8
    pawns_for_site = 12
    white_pawns = []
    black_pawns = []

class InitialState(State):
    def __init__(self):
        self.white_pawns = [Pawn('white', id) for id in range(self.pawns_for_site)]
        self.black_pawns = [Pawn('black', id) for id in range(self.pawns_for_site)]

        black_fields = ((self.board_size**2)//2)
        down_pawns, up_pawns = iter(self.white_pawns), iter(self.black_pawns)
        for i in range(black_fields):
            y = i//(self.board_size//2)
            x = (i%4)*2 + y%2
            try:
                if y in range(0,3):
                    pawn = next(up_pawns)
                    pawn.set_positon((x, y))
                    pawn.set_foreward_vector(1)
                if y in range(5,8):
                    pawn = next(down_pawns)
                    pawn.set_positon((x, y))
                    pawn.set_foreward_vector(-1)
            except StopIteration:
                pass
