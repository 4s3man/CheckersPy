from checkers.board.abstract_game_obj import Game_Obj
class Move(Game_Obj):
    id = 0;
    position_after_move = []
    beated_pawns_id = []
    pawn_id = 0;

    def __init__(pawn_id:int, position_after_move:list, beated_pawns_id:list=[]):
        self.pawn_id = pawn_id
        self.position_after_move = position_after_move
        self.beated_pawns_id = beated_pawns_id
