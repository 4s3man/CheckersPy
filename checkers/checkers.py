from checkers.board.board import *
from checkers.board.move_resolver import *

class Checkers():
    turn = 'white'
    state = None
    move_resolver = None
    max_min = None

    def __init__(self, state: State):
        self.move_resolver = MoveResolver()
        self.state = state
        # self.state = self.move_resolver.resolve_moves(state)

    def resolve_moves(self, collection: str):
        self.state = self.move_resolver.resolve_moves(self.state, collection)

    def make_move(self, pawn_move: dict):
        return True


    def pawn_move_is_valid(self, pawn_move: dict)->bool:
        collection = self.state.white_pawns if pawn_move['pawn']['color'] == 'white' else self.state.black_pawns
        moving_pawn = collection[pawn_move['pawn']['id']]

        return moving_pawn and pawn_move['move'] in moving_pawn.moves
    """TODO TEST THIS"""
    # def make_move(self, pawn: Pawn, move_id: int):
    #     move = pawn.moves[move_id]
    #     enemy_pawns = white_pawns if pawn.color != 'white' else black_pawns
    #     for enemy_pawn in state.enemy_pawns:
    #         if enemy_pawn.id in move.get('beated_pawn_ids', []):
    #             enemy_pawn = None
    #     pawn.y, pawn.x = move['position_after_move']
    #
    #     if pawn.y + pawn.foreward not in range(8):
    #         pawn.type = 'queen'
