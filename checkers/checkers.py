from checkers.board.board import *
from checkers.board.move_resolver import *
from checkers.board.move_resolver_new import MoveResolverNew

from flask import session

class Checkers():
    turn = 'white'
    state = None
    move_resolver = None
    max_min = None

    def __init__(self, state: State):
        self.state = state
        self.move_resolver = MoveResolver()
        # TODO: refractorization
        self.move_resolver_new = MoveResolverNew()


    def resolve_moves(self, collection: str):
        self.state = self.move_resolver.resolve_moves(self.state, collection)

    def make_move(self, id:int, color:str, move:dict):
        self.state = self.state.make_move(id, Color(color), move)

    def pawn_move_is_valid(self, id:int, color:str, move:dict)->bool:
        pawn_collection = self.state.white_pawns if color == 'white' else self.state.black_pawns
        return pawn_collection[id] and move in pawn_collection[id].moves

    def new_resolve_moves(self, pawns_color:Color):
        self.move_resolver_new.resolve_moves(self.state, pawns_color)

    # TODO: refractor
    # def dono(self, session:session):
    #     session['em'] = 'oho'
        # print('ok')
