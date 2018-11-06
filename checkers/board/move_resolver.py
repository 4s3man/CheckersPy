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
        # """debug to remove"""
        # self.get_jump_moves(state.white_pawns[1])
        #
        # """debug to remove"""
        return state

    def resolve_pawn_moves(self, pawn: Pawn):
        if pawn.type == 'normal':
            self.get_moves_for_pawn(pawn)
        # elif pawn.type == 'queen':
        #     self.get_moves_for_queen(pawn)

    def get_moves_for_pawn(self, pawn: Pawn):
        pawn.moves = self.get_jump_moves(pawn) or self.get_pawn_normal_moves(pawn)
        pass

    def get_jump_moves(self, pawn: Pawn):
        pass

    def get_pawn_normal_moves(self, pawn: Pawn):
        pass

    # def have_obligatory_move(self, pawn: Pawn, move: dict):
    #     for y, x in [(1,1), (1,-1), (-1, 1), (-1,-1)]:
    #         try:
    #             pawn_in_direction = self.get_pawn_in_direction(pawn, y, x)
    #             if self.can_jump_in_direction(pawn, pawn_in_direction, y, x, move): return True
    #         except BoardError:
    #             pass
    #     return False

    """Throws NoCoinError, OutOfBoardError"""
    def get_pawn_in_direction(self, pawn: Pawn, y:int, x:int):
        x += pawn.x
        y += pawn.y
        if not self.board.has_position(y, x): raise OutOfBoardError('Field in direction out of the board')
        pawn_in_direction = self.board.fields[y][x]
        if pawn_in_direction is None: raise NoCoinError('No coin in this direction')
        return pawn_in_direction

    # def search_enemy_in_direction(self, pawn:Pawn, y:int, x:int):
    #     board = self.board
    #     if not board.has_position(y, x): raise OutOfBoardError('Field in direction out of the board')
    #     coin_in_direction = board.fields[y][x]
    #     if coin_in_direction is None: raise NoCoinError('No coin in this direction')
    #     return coin_in_direction
