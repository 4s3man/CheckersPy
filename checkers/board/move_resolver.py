from checkers.board.board import *

class MoveResolver():
    board = None

    def __init__(self):
        self.board = Board()
        pass

    def resolve_moves(self, state: State)->State:
        self.board.place_pawns(state)

        for pawn in state.white_pawns + state.black_pawns:
            if pawn: self.resolve_pawn_moves(pawn)

        return state

    def resolve_pawn_moves(self, pawn: Pawn):
        if pawn.type == 'queen':
            self.get_moves_for_queen(pawn)
        elif pawn.type == 'normal':
            self.get_moves_for_normal(pawn)

    def get_moves_for_normal(self, pawn: Pawn):
        pawn.moves = {'beated_coin_ids':[1,1,1,1]}
        
        pass

    # def search_enemy_in_direction(self, pawn:Pawn, y:int, x:int):
    #     board = self.board
    #     if not board.has_position(y, x): raise OutOfBoardError('Field in direction out of the board')
    #     coin_in_direction = board.fields[y][x]
    #     if coin_in_direction is None: raise NoCoinError('No coin in this direction')
    #     return coin_in_direction
