from checkers.board.board import *

class MoveResolver():
    board = None

    def __init__(self):
        pass

    def resolve_moves(self, state: State)->State:
        return state

    def search_enemy_in_direction(self, pawn:Pawn, y:int, x:int):
        board = self.board
        if not board.has_position(y, x): raise OutOfBoardError('Field in direction out of the board')
        coin_in_direction = board.fields[y][x]
        if coin_in_direction is None: raise NoCoinError('No coin in this direction')
        return coin_in_direction
