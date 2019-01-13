from datetime import datetime

class Room():
    creator_id = ''
    joiner_id = ''
    turn = ''
    winner = ''
    board_state = ''
    last_move_time = None
    create_time = None

    def __init__(self, creator_id:int):
        self.creator_id = creator_id
        self.create_time = datetime.now()

    def __repr__(self):
        return str(self.__dict__)
