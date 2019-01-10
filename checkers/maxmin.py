from checkers.board.move_resolver import *
from checkers.board.move_funcs import *
from copy import deepcopy

def pick_computer_move(state:State, color:str)->dict:
    return pick_first_move_with_best_score(
        make_moves_with_scores(state, color)
    )

def make_moves_with_scores(state: State, color: str)->list:
    move_resolver = MoveResolver()
    basic_state = move_resolver.resolve_moves(state, color)
    moves = list(make_moves_gen(state.get_pawns(color)))

    i=0
    for move in make_moves_gen(state.get_pawns(color)):
        score = []
        state = deepcopy(basic_state)
        state = make_move(state, **move[0])
        state = move_resolver.resolve_moves(state, opposite_color(color))
        for move_min in make_moves_gen(state.get_pawns_oposite(color)):
            state = deepcopy(basic_state)
            state = make_move(state, **move_min[0])
            state = move_resolver.resolve_moves(state, color)
            for move_max in make_moves_gen(state.get_pawns(color)):
                score.append(move[1] - move_min[1] + move_max[1])
        """jeśli nie ma score to znaczy że gra zakończyła się w turze przeciwnika
        ustaw wtedy score na nierealnie zły """
        moves[i][1] = max(score) if len(score) else -30
        i += 1
    return moves

def opposite_color(color: str):
    return 'black' if color == 'white' else 'white'

def make_moves_gen(pawns:list):
    for pawn in pawns:
        if pawn is not None:
            for move in pawn.moves:
                yield[{'id':pawn.id, 'color':pawn.color, 'move':move}, len(move.get('beated_pawn_ids', []))]

def pick_first_move_with_best_score(moves_with_scores):
        return sorted(moves_with_scores, key=lambda x: x[1], reverse=True)[0][0] if moves_with_scores else None
