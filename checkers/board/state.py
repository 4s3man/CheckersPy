from checkers.board.abstract_game_obj import Game_Obj
from checkers.board.pawn import Pawn
from checkers.board.color import Color
from copy import deepcopy
import json

class State(Game_Obj):
    board_size = 8
    pawns_for_site = 12
    winner = ''
    white_pawns = [None]*pawns_for_site
    black_pawns = [None]*pawns_for_site

    def __init__(self, jsonState: str = ''):
        """ Construct object from json string or initial state"""
        self.white_pawns = [None] * self.pawns_for_site
        self.black_pawns = [None] * self.pawns_for_site
        if jsonState:
            self.json_decode(jsonState)
        else:
            self.set_initial_state()

    def set_initial_state(self):
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

    def json_encode(self):
        return json.dumps(self, default=(lambda x: x.__dict__))

    def json_decode(self, stateJson: str):
        stateDict = json.loads(stateJson)
        for pawn in stateDict['white_pawns'] + stateDict['black_pawns']:
            self.makePawn(pawn)

    def makePawn(self, pawn: dict):
        if pawn is None: return
        i = pawn['id']
        pawns = self.white_pawns if pawn['color'] == 'white' else self.black_pawns
        pawns[i] = Pawn(pawn['color'], i, pawn['type'])
        pawns[i].set_positon(pawn['y'], pawn['x'])
        pawns[i].set_foreward_vector(pawn['foreward'])
        pawns[i].set_moves(pawn.get('moves', []))

    def make_move(self, id:int, color:Color, move:dict):
        new_state = deepcopy(self)
        our_pawns = new_state.get_pawn_collection(color)
        enemy_pawns = new_state.get_pawn_collection(color.opposite())

        next_y, next_x = move['position_after_move']
        our_pawns[id].set_positon(next_y, next_x)
        if our_pawns[id].should_become_queen():
            our_pawns[id].type = 'queen'

        for enemy in enemy_pawns:
            if enemy and enemy.id in move.get('beated_pawn_ids', []):
                enemy_pawns[enemy.id] = None

        return new_state

    def has_only_queens(self)->bool:
        for pawn in self.black_pawns + self.white_pawns:
            if pawn is not None and pawn.type != 'queen':
                return False;
        return True

    def collection_has_moves(self, color:Color)->bool:
        pawn_collection = get_pawn_collection(color)
        for pawn in pawn_collection:
            if pawn is not None and len(pawn.moves)>0:return True
        return False

    def get_pawn_collection(self, color:Color)->list:
        return self.white_pawns if color.name == 'WHITE' else self.black_pawns
    
    def get_winner(self)->str:
        """Returns white, black or empty string"""
        lost_state = [None for x in range(12)]
        if lost_state == self.white_pawns: return 'black'
        elif lost_state == self.black_pawns: return 'white'
        else: return ''
