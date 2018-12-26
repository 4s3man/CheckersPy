from checkers.board.abstract_game_obj import Game_Obj
class Pawn(Game_Obj):
    id = 0
    color = ''
    foreward = 0
    type = ''
    moves = []
    x = 0
    y = 0
    def __init__(self, color:str, id:int, type:str='normal'):
        self.color = color
        self.id = id
        self.type = type
        self.moves = []

    """direction for coin normal moves"""
    def set_foreward_vector(self, vector:int):
        self.foreward = vector

    """sets coin position: y, x"""
    def set_positon(self, y:int, x:int):
        self.x = x
        self.y = y

    """sets coin moves"""
    def set_moves(self, moves:list):
        self.moves = moves
