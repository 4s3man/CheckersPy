import pytest
from checkers.room_index import *
from uuid import uuid4

@pytest.fixture()
def waiting_room():
    return Room('waiting room')

@pytest.fixture()
def old_waiting_room():
    room = Room('old waiting room')
    room.create_time = datetime.now() - (Room.time_for_join + timedelta(seconds=10))
    return room

@pytest.fixture()
def too_long_without_moving_room()-> Room:
    id = uuid4().hex
    room = Room(id)
    room.joiner_id = uuid4().hex
    room.last_move_time = datetime.now() - (Room.time_for_move + timedelta(seconds=5))
    room.joiner_id = uuid4().hex

    return room

@pytest.fixture()
def creator_winned_room()-> Room:
    room = Room('creator_winned_room')
    room.joiner_id = uuid4().hex
    room.winner = 'creator_winned_room'
    return room

@pytest.fixture()
def old_unwinned_room()-> Room:
    room = Room('old unwinned room')
    room.joiner_id = uuid4().hex
    room.last_move_time = datetime(2019, 1, 13, 11, 45, 33)
    room.turn = 'old unwinned room'
    return room

@pytest.fixture()
def old_winned_room()-> Room:
    room = Room('old winned room')
    room.joiner_id = uuid4().hex
    room.last_move_time = datetime(2019, 1, 13, 11, 45, 33)
    room.turn = 'old winned room'
    room.winner = 'old winned room'
    return room

@pytest.fixture()
def roomIndex_all_kind_of_rooms(
    waiting_room,
    too_long_without_moving_room,
    creator_winned_room,
    old_unwinned_room,
    old_winned_room
):
    roomIndex = RoomIndex()
    rooms = [
        waiting_room,
        too_long_without_moving_room,
        creator_winned_room,
        old_unwinned_room,
        old_winned_room
    ]
    for room in rooms:
        id = uuid4().hex
        roomIndex[id] = room

    return roomIndex
