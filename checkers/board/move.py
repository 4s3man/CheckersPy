from checkers.board.abstract_game_obj import Game_Obj
from itertools import count

class Move(Game_Obj):
    _ids = count(1);
    position_after_move = []
    beated_pawns_id = []
    pawn_id = 0;

    def __init__(self, pawn_id:int, visited_fields:list, beated_pawn_ids:list=[]):
        self.id = next(self._ids)
        self.pawn_id = pawn_id
        self.visited_fields = visited_fields
        self.beated_pawn_ids = beated_pawn_ids
