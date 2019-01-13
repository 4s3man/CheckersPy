import pytest
from checkers.room_index import *
from uuid import uuid4

def test_count_joinable(waiting_room, creator_winned_room, old_winned_room, old_unwinned_room):
    input = [waiting_room, creator_winned_room, old_winned_room, old_unwinned_room]
    rooms = RoomIndex()
    for id, room in ((uuid4().hex, room) for room in input):
        rooms[id] = room

    assert 1 == rooms.count_joinable()

def test_set_item_instance(waiting_room):
    rooms = RoomIndex()

    with pytest.raises(InvalidArgument):
        rooms[uuid4().hex] = 'fuk'

    id = uuid4().hex
    rooms[id] = waiting_room
    assert rooms[id].create_time != ''
    assert rooms[id].creator_id != ''

def test_get_free_room_id(waiting_room):
    rooms = RoomIndex()
    id = uuid4().hex
    rooms[id] = waiting_room

    assert rooms.get_free_room_id() == id


def test_join_room(waiting_room):
    rooms = RoomIndex()
    id = uuid4().hex
    rooms[id] = waiting_room

    pid = uuid4().hex
    rooms.join_room(id, pid)
    assert rooms[id].joiner == pid
