from datetime import datetime

class Room():
    creator_id = ''
    joiner_id = ''
    turn = ''
    winner = ''
    board_state = ''
    draw_count = 0
    last_move_time = None
    create_time = None

    def __init__(self, creator_id:int):
        self.creator_id = creator_id
        self.create_time = datetime.now()
        self.turn = creator_id

    def __repr__(self):
        return str(self.__dict__)

    def get_turn_color(self):
        return 'white' if self.turn == self.creator_id else 'black'

    def change_turn(self):
        self.turn = self.creator_id if self.turn == self.joiner_id else self.joiner_id
