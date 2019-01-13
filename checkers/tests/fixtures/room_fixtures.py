import pytest
from checkers.room_index import *
from uuid import uuid4

@pytest.fixture()
def waiting_room():
    return Room('b210693687a04d41807f9b97eca6b4c6')

@pytest.fixture()
def creator_winned_room():
    room = Room('b210693687a04d41807f9b97eca6b4c6')
    room.joiner_id = uuid4().hex
    room.winner = 'b210693687a04d41807f9b97eca6b4c6'
    return room

@pytest.fixture()
def old_unwinned_room():
    room = Room('b210693687a04d41807f9b97eca6b4c6')
    room.joiner_id = uuid4().hex
    room.last_move_time = '2019-01-13 11:45:33.791333'
    room.turn = 'b210693687a04d41807f9b97eca6b4c6'
    return room

@pytest.fixture()
def old_winned_room():
    room = Room('b210693687a04d41807f9b97eca6b4c6')
    room.joiner_id = uuid4().hex
    room.last_move_time = '2019-01-13 11:45:33.791333'
    room.turn = 'b210693687a04d41807f9b97eca6b4c6'
    room.winner = 'b210693687a04d41807f9b97eca6b4c6'
    return room