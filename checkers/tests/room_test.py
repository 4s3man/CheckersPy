import pytest
from checkers.room import Room
from datetime import datetime

def test_is_time_up_for_move(
        too_long_without_moving_room,
        waiting_room,
        creator_winned_room
):
    now = datetime.now()
    assert too_long_without_moving_room.is_time_up_for_move(now) == True
    assert waiting_room.is_time_up_for_move(now) == False

def test_is_joined(
        too_long_without_moving_room,
        waiting_room,
        creator_winned_room
):
    assert too_long_without_moving_room.is_waiting() == False
    assert creator_winned_room.is_waiting() == False

    assert waiting_room.is_waiting() == True

def test_is_winned(
        old_winned_room,
        old_unwinned_room
):
    assert old_winned_room.is_winned() == True
    assert old_unwinned_room.is_winned() == False


def test_is_old_winned(
        old_winned_room,
        old_unwinned_room
):
    now = datetime.now()
    assert old_winned_room.is_old_winned(now) == True
    assert old_unwinned_room.is_old_winned(now) == False

def test_is_old_waiting(
        waiting_room,
        old_waiting_room
):
    now = datetime.now()
    assert old_waiting_room.is_old_waiting(now) == True
    assert waiting_room.is_old_waiting(now) == False
