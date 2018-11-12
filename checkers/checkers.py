from checkers.board.board import *
from checkers.board.move_resolver import *

class Checkers():
    turn = 'white'
    state = None
    move_resolver = None
    max_min = None

    def __init__(self, state: State):
        self.move_resolver = MoveResolver()
        self.state = self.move_resolver.resolve_moves(state)

    """TODO TEST THIS"""
    def make_move(self, pawn: Pawn, move_id: int):
        move = pawn.moves[move_id]
        enemy_pawns = white_pawns if pawn.color != 'white' else black_pawns
        for enemy_pawn in state.enemy_pawns:
            if enemy_pawn.id in move.get('beated_pawn_ids', []):
                enemy_pawn = None
        pawn.y, pawn.x = move['positon_after_move']

        if pawn.y + pawn.foreward not in range(8):
            pawn.type = 'queen'
