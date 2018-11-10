from checkers.board.board import *
import copy

class MoveResolver():
    board = None
    directions = [(1,1), (1,-1), (-1, -1), (-1,1)]

    def __init__(self, state: State = None):
        self.board = Board()
        if state:
            self.board.place_pawns(state)

    def resolve_moves(self, state: State)->State:
        self.board.place_pawns(state)
        # pawn = state.white_pawns[2]
        # pawn.moves = self.get_moves_for_pawn(pawn)

        # for pawn in state.white_pawns + state.black_pawns:
        #     if pawn: self.resolve_pawn_moves(pawn)
        # """debug to remove"""
        # self.get_jump_moves(state.white_pawns[1])
        #
        # """debug to remove"""
        return state

    # def resolve_pawn_moves(self, pawn: Pawn):
    #     if pawn.type == 'normal':
    #         self.get_moves_for_pawn(pawn)
    #     # elif pawn.type == 'queen':
    #     #     self.get_moves_for_queen(pawn)

    def get_moves_for_queen(self, pawn:Pawn)->list:
        pass

    def get_moves_for_pawn(self, pawn: Pawn)-> list:
        return self.get_most_beating_moves(self.get_jump_moves(pawn, [])) or self.get_normal_pawn_moves(pawn)

    def get_jump_moves(self, pawn: Pawn, move_list: list, move: dict={})-> list:
        if self.pawn_has_obligatory_move(pawn, move):
            for y, x in self.directions:
                try:
                    pawn_in_direction = self.get_pawn_in_direction(pawn, (y, x))
                    if self.pawn_can_jump_in_direction(pawn, pawn_in_direction, (y, x), move):
                        next_y, next_x = pawn_in_direction.y + y, pawn_in_direction.x + x

                        move_inst = {'positon_after_move':None, 'beated_pawn_ids':[]} if not len(move) else copy.deepcopy(move)
                        move_inst['beated_pawn_ids'].append(pawn_in_direction.id)

                        pawn1 = copy.deepcopy(pawn)
                        pawn1.y = next_y
                        pawn1.x = next_x

                        if move_inst not in move_list\
                        and not self.pawn_has_obligatory_move(pawn1, move_inst)\
                        and not self.same_pawns_beated(move_inst, move_list):
                            move_inst['positon_after_move'] = (next_y, next_x)
                            move_list.append(move_inst)

                        self.get_jump_moves(pawn1, move_list, move_inst)
                except BoardError:
                    pass
        return move_list

    def get_normal_pawn_moves(self, pawn: Pawn)-> list:
        move_list = []
        for y,x in [(pawn.foreward, 1), (pawn.foreward, -1)]:
            try:
                self.get_pawn_in_direction(pawn, (y, x))
            except NoCoinError:
                move = {"positon_after_move":(pawn.y + y, pawn.x + x)}
                move_list.append(move)
            except OutOfBoardError:
                pass
        return move_list

    def pawn_has_obligatory_move(self, pawn: Pawn, move: dict = {})->bool:
        for y, x in self.directions:
            try:
                pawn_to_check = self.get_pawn_in_direction(pawn, (y, x))
                if self.pawn_can_jump_in_direction(pawn, pawn_to_check, (y, x), move): return True
            except BoardError:
                pass
        return False

    def get_pawn_in_direction(self, pawn: Pawn, direction: tuple)->Pawn:
        """Throws NoCoinError, OutOfBoardError or gets pawn in direction"""
        y,x = direction
        x += pawn.x
        y += pawn.y
        if not self.board.has_position(y, x): raise OutOfBoardError('Field in direction out of the board')
        pawn_in_direction = self.board.fields[y][x]
        if pawn_in_direction is None: raise NoCoinError('No coin in this direction')
        return pawn_in_direction

    def pawn_can_jump_in_direction(self, this_pawn: Pawn, pawn_to_check: Pawn, vector: tuple, move: dict):
        """false if position after jump is out of board"""
        y, x = (v*2 for v in vector)
        if not self.board.has_position(this_pawn.y + y, this_pawn.x + x): return False
        """false if pawns have same colors"""
        if pawn_to_check.color == this_pawn.color: return False

        """false if on field after jump is pawn and it's not the pawn who jumps"""
        field_after_jump = self.board.fields[this_pawn.y + y][this_pawn.x + x]
        if isinstance(field_after_jump, Pawn)\
        and (field_after_jump.id != this_pawn.id)\
        and (field_after_jump.color != this_pawn.color): return False

        """false if move is calculating and coin_in_direction was already beated"""
        if len(move) and (pawn_to_check.id in move['beated_pawn_ids']): return False

        return True

    def same_pawns_beated(self, move: dict, move_list: list)-> bool:
        for move_l in move_list:
            if set(move_l['beated_pawn_ids']) == set(move['beated_pawn_ids']): return True
        return False

    def get_most_beating_moves(self, move_list: list)->list:
        """Returns list of moves which has longest beated_pawn_ids"""
        if len(move_list):
            max_beated_pawns = len(max(move_list, key=lambda x: len(x['beated_pawn_ids']))['beated_pawn_ids'])
            return [move for move in move_list if len(move['beated_pawn_ids']) == max_beated_pawns]
        else:
            return move_list
