from checkers.board.pawn import *

def test_eq():
    pawn1 = Pawn('white', 1, 'queen')
    pawn2 = Pawn('white', 1)
    pawn3 = Pawn('white', 1)

    assert False == (pawn1 == pawn2)
    assert True == (pawn2 == pawn3)
