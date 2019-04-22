from checkers.room import Room
from datetime import datetime, timedelta
from checkers.board.state import *
import json

class InvalidArgument(Exception):
    pass
class TooManyRoomsAtOnce(Exception):
    pass

class RoomIndex(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, Room): raise InvalidArgument('RoomIndex accepts only arguments of type Room')
        if len(self) >= 1000: TooManyRoomsAtOnce()
        super().__setitem__(key, value)

    def count_joinable(self)->int:
        count = 0
        for room in self.values():
            if room.joiner_id == '': count += 1
        return count

    def get_free_room_id(self)->str:
        for id, room in self.items():
            if room.joiner_id == '':
                return id
        return ''

    def join_room(self, room_id:str, joiner_id: str):
        self[room_id].joiner_id = joiner_id

    def room_exists(self, room_id: str)->bool:
        return room_id in self.keys()

    def cultivate(self):
        now = datetime.now()
        self.delete_old_unjoined_or_winned(now)
        self.win_too_long_unmoved(now)

    def delete_old_unjoined_or_winned(self, now: datetime):
        ids = [id for (id, room) in self.items() if room.is_old_waiting(now) or room.is_old_winned(now)]
        for id in ids:
            del self[id]

    def win_too_long_unmoved(self, now: datetime):
        ids = [id for (id, room) in self.items() if room.is_old_waiting(now)]
        for id in ids:
            self[id].win_too_long_unmoved(now)
