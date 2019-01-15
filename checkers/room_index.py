from checkers.room import Room
import datetime
from checkers.board.state import *
import json

class InvalidArgument(Exception):
    pass
class TooManyRoomsAtOnce(Exception):
    pass

class RoomIndex(dict):
    """room lasts for this amount of seconds if"""
    """already winned"""
    winned_room_duration = 1 * 60

    """created and nobody joined"""
    waiting_room_duration = 10 * 60

    """room will be set to won for not currently moving if time from last move was
    grater than 40 sec"""
    time_after_last_move = 40


    def __setitem__(self, key, value):
        if not isinstance(value, Room): raise InvalidArgument('Do rooms można dodawać tylko obiekt typu room')
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

    #todo przetestować usuwanie rzeczy z room index nie jest teraz najważniejsz zostawić na potem
    def delete_too_long_waiting_for_join(self):
        waiting_rooms_to_delete = (id for (id, room) in self.items() if room.joiner_id=='' and (datetime.now() - room.create_time).seconds > self.winned_room_duration)
        for id in (id for (id, room) in self.items() if (datetime.now() - room.create_time).seconds > self.winned_room_duration):
            del self[id]