from checkers.board.state import State
from checkers.board.pawn import Pawn
from functools import reduce
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
        if enemy and enemy.id in move.get('beated_pawn_ids', []):
            enemy_pawns[enemy.id] = None

    return new_state

def pawn_should_become_queen(pawn:Pawn):
    if pawn.foreward == 1 and pawn.y == 7 and pawn.type != 'queen':
        return True
    if pawn.foreward == -1 and pawn.y == 0 and pawn.type != 'queen':
        return True
    return False

def win(state:State)->bool:
    lost_pawns = [None for x in range(13)]
    if not (hasattr(win,'id')): win.id = 0
    if state.white_pawns == lost_pawns or state.black_pawns == lost_pawns:
        win.id = 0;
        return True
    elif has_only_queens(state):
        win.id +=1;
        if(win.id == 6):
            return True
    else:
        return False

def has_only_queens(state:State)->bool:
    for pawn in state.black_pawns + state.white_pawns:
        if pawn is not None and pawn.type != 'queen':
            return False;
    return True
