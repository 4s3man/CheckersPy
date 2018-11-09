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
        moves = self.get_jump_moves_for_pawn(state.white_pawns[1], [])
        print(moves)
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
    #
    # def get_moves_for_pawn(self, pawn: Pawn):
    #     pawn.moves = self.get_jump_moves(pawn) or self.get_pawn_normal_moves(pawn)
    #     pass
    #
    # def get_jump_moves(self, pawn: Pawn):
    #     pass
    #
    # def get_pawn_normal_moves(self, pawn: Pawn):
    #     pass

    def get_jump_moves_for_pawn(self, pawn: Pawn, move_list: list, move: dict={}, debug=0)-> list:
        """debug on circle"""
        if self.pawn_has_obligatory_move(pawn, move):
            for y, x in self.directions:
                try:
                    pawn_in_direction = self.get_pawn_in_direction(pawn, (y, x))
                    if self.pawn_can_jump_in_direction(pawn, pawn_in_direction, (y, x), move):
                        next_y, next_x = pawn_in_direction.y + y, pawn_in_direction.x + x

                        move_inst = {'pos':[], 'beated_pawn_ids':[]} if not len(move) else copy.deepcopy(move)
                        move_inst['pos'].append((next_y, next_x))
                        move_inst['beated_pawn_ids'].append(pawn_in_direction.id)

                        pawn1 = copy.deepcopy(pawn)
                        pawn1.y = next_y
                        pawn1.x = next_x

                        if move_inst not in move_list\
                        and not self.pawn_has_obligatory_move(pawn1, move_inst)\
                        and not self.same_pos_in_movelist(move_inst, move_list):
                            move_list.append(move_inst)

                        self.get_jump_moves_for_pawn(pawn1, move_list, move_inst)
                except BoardError:
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

    def same_pos_in_movelist(self, move: dict, move_list: list)-> bool:
        for move_l in move_list:
            if set(move_l['pos']) == set(move['pos']): return True
        return False
