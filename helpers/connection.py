import re
import json
from helpers.connection_exceptions import *

"""
Throws:
EmptyPawnMove
InvalidPawnMove exceptions
"""
def receive_pawn_move(pawn_move: dict, turn:str)->dict:
    if(not len(pawn_move)): raise EmptyPawnMove('Move is empty')
    if(type(pawn_move) is not dict): raise InvalidPawnMove('Posted data is not dict')
    try:
        assert turn == pawn_move['color']
        assert len(pawn_move) == 3
        assert pawn_move['id'] in range(12)
        assert pawn_move['color'] in ['white', 'black']

        assert len(pawn_move['move']) <= 2

        assert len(pawn_move['move']['position_after_move']) == 2
        assert pawn_move['move']['position_after_move'][0] in range(8)
        assert pawn_move['move']['position_after_move'][1] in range(8)

        beated_pawn_ids = pawn_move['move'].get('beated_pawn_ids', [])
        assert len(beated_pawn_ids) < 13
        for beated_pawn_id in beated_pawn_ids:
            assert beated_pawn_id in range(12)
    except (KeyError, AssertionError) as e:
        raise InvalidPawnMove('Posted data does not have required pawn_move data')
    return pawn_move

def strip_redundant_for_frontend(json_state:str)->str:
    return re.sub(
            ',\s+}','}',
            re.sub('"moves": \[\],{0,1}|"foreward": (-\d|\d),{0,1}','', json_state)
           )
