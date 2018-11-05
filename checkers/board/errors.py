class BoardError(Exception):
    pass

class NoCoinError(BoardError):
    pass

class OutOfBoardError(BoardError):
    pass
