from checkers.board.board import *
from checkers.board.color import Color
from checkers.board.move import Move
import copy

class MoveResolverNew():
    board = None
    directions = [(1,1), (1,-1), (-1, -1), (-1,1)]

    def __init__(self, state: State = None):
        self.board = Board()
        if state:
            self.board.place_pawns(state)

    def resolve_moves(self, state: State, pawns_color: Color)->list:
        self.board.place_pawns(state)
        pawn_collection = state.get_pawn_collection(pawns_color)
        moves = self.resolve_moves_for_pawn_collection(pawn_collection)

        for move in moves:
            print(move.id, ':', move.pawn_id, ':', move.visited_fields, ';', move.beated_pawn_ids)
        # self.leave_max_beating_moves_only(collection)
        return moves

    def resolve_moves_for_pawn_collection(self, pawn_collection: list)->list:
        moves = []
        for pawn in pawn_collection:
            if pawn:
                if pawn.type == 'normal':
                    moves.append(*self.get_moves_for_pawn(pawn))
                elif pawn.type == 'queen':
                    moves.append(*self.get_moves_for_queen(pawn))
                else:
                    pass
        return moves

    # TODO: refractor for moves
    def leave_max_beating_moves_only(self, pawn_collection: list):
        """
        Modifies pawn collection so it has only moves who beat biggest amount of pawns
        if there are no beating moves it leaves all of them
        important for performance, and becouse most beating moves are obligatory according to rules
        """
        max_beated_pawns = max(
                map(
                    lambda pawn: self.get_max_beated_pawns_from_move_list(pawn.moves) if pawn != None else 0,
                     pawn_collection
                    )
             )
        for pawn in pawn_collection:
            if pawn:
                pawn.moves = list(
                                filter(
                                    lambda moves:len(moves.get('beated_pawn_ids', [])) == max_beated_pawns,
                                    pawn.moves
                                    )
                                )

    def get_moves_for_queen(self, queen: Pawn)->list:
        return self.get_most_beating_moves(self.get_queen_jump_moves(queen)) or self.get_queen_normal_moves(queen)

    def get_moves_for_pawn(self, pawn: Pawn)-> list:
        return self.get_most_beating_moves(self.get_jump_moves(pawn, [])) or self.get_normal_pawn_moves(pawn)

    # TODO: refractor move
    def get_queen_jump_moves(self, pawn:Pawn)->list:
        move_list = []
        for y, x in self.directions:
            virtual_queen = copy.deepcopy(pawn)
            pawn_in_line = self.get_pawn_in_line(virtual_queen, (y, x))
            if pawn_in_line:
                virtual_queen.y = pawn_in_line.y - y
                virtual_queen.x = pawn_in_line.x - x
                if self.pawn_can_jump_in_direction(virtual_queen, pawn_in_line, (y,x), {}):
                    virtual_queen.y = pawn_in_line.y + y
                    virtual_queen.x = pawn_in_line.x + x
                    jump_moves = self.get_jump_moves(virtual_queen, [], {'position_after_move':None, 'beated_pawn_ids':[pawn_in_line.id]})
                    if jump_moves:
                        move_list += jump_moves
                    else:
                        move_list.append({'position_after_move':[pawn_in_line.y+y, pawn_in_line.x+x], 'beated_pawn_ids':[pawn_in_line.id]})
        return move_list

    # TODO: refractor move
    def get_queen_normal_moves(self, this_pawn: Pawn)->list:
        move_list = []
        for direction in self.directions:
            for i in range(1,self.board.board_size + 1):
                y,x = (d*i for d in direction)
                try:
                    pawn_in_line = self.get_pawn_in_direction(this_pawn, (y,x))
                    if pawn_in_line:
                        break
                except NoCoinError:
                    move_list.append({'position_after_move':[this_pawn.y + y, this_pawn.x + x]})
                except OutOfBoardError:
                    pass
        return move_list

    def get_pawn_in_line(self, this_pawn: Pawn, direction: tuple)->Pawn:
        for i in range(1,self.board.board_size + 1):
            y,x = (d*i for d in direction)
            try:
                return self.get_pawn_in_direction(this_pawn, (y,x))
            except NoCoinError:
                pass
            except OutOfBoardError:
                return None

    def get_jump_moves(self, pawn: Pawn, move_list: list, move: dict={})-> list:
        if self.pawn_has_obligatory_move(pawn, move):
            for y, x in self.directions:
                try:
                    pawn_in_direction = self.get_pawn_in_direction(pawn, (y, x))
                    if self.pawn_can_jump_in_direction(pawn, pawn_in_direction, (y, x), move):
                        next_y, next_x = pawn_in_direction.y + y, pawn_in_direction.x + x

                        carrier = {'visited_fields':[], 'beated_pawn_ids':[]} if not len(move) else copy.deepcopy(move)
                        carrier['beated_pawn_ids'].append(pawn_in_direction.id)

                        pawn1 = copy.deepcopy(pawn)
                        pawn1.y = next_y
                        pawn1.x = next_x

                        carrier['visited_fields'].append([next_y, next_x])

                        if carrier not in move_list\
                        and not self.pawn_has_obligatory_move(pawn1, carrier)\
                        and not self.same_pawns_beated(carrier, move_list):
                            moveI = Move(pawn.id, carrier['visited_fields'], carrier['beated_pawn_ids'])
                            move_list.append(moveI)

                        self.get_jump_moves(pawn1, move_list, carrier)
                except BoardError:
                    pass
        return move_list

    # TODO: refractor
    def get_normal_pawn_moves(self, pawn: Pawn)-> list:
        move_list = []
        for y,x in [(pawn.foreward, 1), (pawn.foreward, -1)]:
            try:
                self.get_pawn_in_direction(pawn, (y, x))
            except NoCoinError:
                move_list.append(
                    Move(pawn.id, [pawn.y + y, pawn.x + x])
                )
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

    def pawn_can_jump_in_direction(self, this_pawn: Pawn, pawn_to_check: Pawn, vector: tuple, move: dict)->bool:
        """false if position after jump is out of board"""
        y, x = (v*2 for v in vector)
        if not self.board.has_position(this_pawn.y + y, this_pawn.x + x): return False
        """false if pawns have same colors"""
        if pawn_to_check.color == this_pawn.color: return False

        """false if on field after jump is pawn and it's not the pawn who jumps"""
        field_after_jump = self.board.fields[this_pawn.y + y][this_pawn.x + x]

        """false if on field after jump is pawn and its not same pawn who jumps"""
        if isinstance(field_after_jump, Pawn):
            if not (field_after_jump.id == this_pawn.id and field_after_jump.color == this_pawn.color): return False

        """false if move is calculating and coin_in_direction was already beated"""
        if len(move) and (pawn_to_check.id in move['beated_pawn_ids']): return False

        return True

    def same_pawns_beated(self, move: dict, move_list: list)-> bool:
        for move_l in move_list:
            if set(move_l.beated_pawn_ids) == set(move['beated_pawn_ids']): return True
        return False

    def get_most_beating_moves(self, move_list: list)->list:
        """Returns list of moves which has longest beated_pawn_ids"""
        if len(move_list):
            max_beated_pawns = self.get_max_beated_pawns_from_move_list(move_list)
            return [move for move in move_list if len(move.beated_pawn_ids) == max_beated_pawns]
        else:
            return move_list

    def get_max_beated_pawns_from_move_list(self, move_list: list)->int:
        if len(move_list):
            return len(max(move_list, key=lambda x: len(x.beated_pawn_ids)).beated_pawn_ids)
        else:
            return 0
