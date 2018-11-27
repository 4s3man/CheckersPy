from checkers.board.state import State
from checkers.board.pawn import Pawn
import copy

def make_move(state:State, id:int, color:str, move:dict):
    new_state = copy.deepcopy(state)
    our_pawns = new_state.white_pawns if color == 'white' else new_state.black_pawns
    enemy_pawns = new_state.white_pawns if color != 'white' else new_state.black_pawns

    next_y, next_x = move['position_after_move']
    our_pawns[id].set_positon(next_y, next_x)
    if pawn_should_become_queen(our_pawns[id]):
        our_pawns[id].type = 'queen'

    for enemy in enemy_pawns:
        if enemy in move.get('beated_pawn_ids', []):
            enemy = None

    return new_state

def pawn_should_become_queen(pawn:Pawn):
    if pawn.foreward == 1 and pawn.y == 7 and pawn.type != 'queen':
        return True
    if pawn.foreward == -1 and pawn.y == 0 and pawn.type != 'queen':
        return True
    return False
