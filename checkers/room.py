from datetime import datetime, timedelta

class Room():
    """room lasts for this amount of seconds if"""
    """already winned"""
    last_after_win = timedelta(minutes=1)

    """created and nobody joined"""
    time_for_join = timedelta(minutes=1)

    """room will be set to won for not currently moving if time from last move was
    grater than 40 sec"""
    time_for_move = timedelta(seconds=40)

    creator_id = ''
    joiner_id = ''
    turn = ''
    winner = ''
    board_state = ''
    draw_count = 0
    last_move_time = None
    create_time = None

    def __init__(self, creator_id: int):
        self.last_move_time = None
        self.creator_id = creator_id
        self.create_time = datetime.now()
        self.turn = creator_id
        self.winner = ''

    def __repr__(self):
        return str(self.__dict__)

    def change_turn(self):
        self.last_move_time = datetime.now()
        self.turn = self.creator_id if self.turn == self.joiner_id else self.joiner_id

    def get_turn_color(self)-> str:
        return 'white' if self.turn == self.creator_id else 'black'

    def win_too_long_unmoved(self):
        self.change_turn()
        self.winner = self.turn

    def is_time_up_for_move(self, now: datetime)-> bool:
        if None is self.last_move_time:
            return False
        return (now - self.last_move_time) > self.time_for_move

    def is_waiting(self)-> bool:
        return self.joiner_id == ''

    def is_old_winned(self, now: datetime)-> bool:
        if self.last_move_time is None:
            return False
        return self.is_winned() and ((now - self.last_move_time) > self.last_after_win)

    def is_old_waiting(self, now: datetime)-> bool:
        return self.is_waiting() and ((now - self.create_time) > self.time_for_join)

    def is_winned(self)-> bool:
        return self.winner != ''
