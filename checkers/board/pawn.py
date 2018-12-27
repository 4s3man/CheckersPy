from checkers.board.abstract_game_obj import GameObj
class Pawn(GameObj):
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

    def set_foreward_vector(self, vector:int):
        """direction for coin normal moves"""
        self.foreward = vector

    def set_positon(self, y:int, x:int):
        """sets coin position: y, x"""
        self.x = x
        self.y = y

    def set_moves(self, moves:list):
        """sets coin moves"""
        self.moves = moves

    def should_become_queen(self):
        if self.foreward == 1 and self.y == 7 and self.type != 'queen':
            return True
        if self.foreward == -1 and self.y == 0 and self.type != 'queen':
            return True
        return False
