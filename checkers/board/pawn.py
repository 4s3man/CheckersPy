class Pawn:
    id = 0
    color = ''
    foreward = 0
    type = ''
    moves = {}
    x = 0
    y = 0
    def __init__(self, color:str, id:int, type:str='normal'):
        self.color = color
        self.id = id
        self.type = type

    """direction for coin normal moves"""
    def set_foreward_vector(self, vector:int):
        self.foreward = vector

    """position: (x,y)"""
    def set_positon(self, position:tuple):
        self.x, self.y = position

    """sets coin moves"""
    def set_moves(self, moves:dict):
        self.moves = moves
