from checkers.board.pawn import Pawn
import json

class State():
    board_size = 8
    pawns_for_site = 12
    winner = ''
    def __init__(self, jsonState: str = ''):
        self.white_pawns = [None] * self.pawns_for_site
        self.black_pawns = [None] * self.pawns_for_site
        if jsonState:
            self.json_decode(jsonState)

    def __eq__(self, other: object):
        this_obj = json.loads(json.dumps(self, default=(lambda x: x.__dict__)))
        other_obj = json.loads(json.dumps(other, default=(lambda x: x.__dict__)))
        return this_obj == other_obj

    def get_winner(self)->str:
        """Returns white, black or empty string"""
        lost_state = [None for x in range(12)]
        if lost_state == self.white_pawns: return 'black'
        elif lost_state == self.black_pawns: return 'white'
        else: return ''

    def json_encode(self):
        return json.dumps(self, default=(lambda x: x.__dict__))

    def json_decode(self, stateJson: str):
        stateDict = json.loads(stateJson)
        pawns = stateDict['white_pawns'] + stateDict['black_pawns']
        for pawn in pawns:
            self.makePawn(pawn)

    def makePawn(self, pawn: dict):
        if pawn is None: return
        i = pawn['id']
        collection = self.white_pawns if pawn['color'] == 'white' else self.black_pawns
        collection[i] = Pawn(pawn['color'], i, pawn['type'])
        collection[i].set_positon(pawn['y'], pawn['x'])
        collection[i].set_foreward_vector(pawn['foreward'])
        collection[i].set_moves(pawn.get('moves', []))

class InitialState(State):
    def __init__(self):
        self.white_pawns = [Pawn('white', id) for id in range(self.pawns_for_site)]
        self.black_pawns = [Pawn('black', id) for id in range(self.pawns_for_site)]

        black_fields = ((self.board_size**2)//2)
        down_pawns, up_pawns = iter(self.white_pawns), iter(self.black_pawns)
        for i in range(black_fields):
            y = i//(self.board_size//2)
            x = (i%4)*2 + y%2
            try:
                if y in range(0,3):
                    pawn = next(up_pawns)
                    pawn.set_positon(y, x)
                    pawn.set_foreward_vector(1)
                if y in range(5,8):
                    pawn = next(down_pawns)
                    pawn.set_positon(y, x)
                    pawn.set_foreward_vector(-1)
            except StopIteration:
                pass
