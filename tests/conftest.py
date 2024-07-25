import pytest

from talaka_kombat_jrpg.player import Player


@pytest.fixture
def player_1_name():
    return "Tony"


@pytest.fixture
def player_1(player_1_name):
    return Player(player_name=player_1_name)


@pytest.fixture
def player_2_name():
    return "Arnold"


@pytest.fixture
def player_2(player_2_name):
    return Player(player_name=player_2_name)
