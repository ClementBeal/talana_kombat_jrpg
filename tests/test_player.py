import pytest
from talaka_kombat_jrpg.player import ButtonCombination, Player, Skill


@pytest.fixture
def player(player_1: Player):
    return player_1


class MockSkill(Skill):
    def __init__(self) -> None:
        super().__init__(
            2,
            ButtonCombination([], []),
        )

    def get_dammage_message(self, origin_player: Player, target_player: Player) -> str:
        return ""


@pytest.fixture
def skill():
    return MockSkill()


def test_player__init():
    player_name = "Tony"
    player = Player(player_name=player_name)

    assert player.player_name == player_name
    assert player.energy == 6


def test_player__add_skill(player: Player, skill: Skill):
    player.add_skill(skill)

    assert len(player.skills) == 1
    assert player.skills[0] == skill


def test_player__is_dead(player: Player):
    player = Player("Player 1")

    assert not player.is_dead()

    player.energy = 0

    assert player.is_dead()


def test_player__is_dead__negative_value(player: Player):
    assert not player.is_dead()

    player.energy = -2

    assert player.is_dead()


def test_player__receive_dammage(player: Player, skill: Skill):
    player.receive_dammage(skill)

    assert player.energy == 4


def test_player__attack(player: Player, skill: Skill):
    target_player = Player("Target")

    player.attack(target_player, skill)

    assert target_player.energy == 4
