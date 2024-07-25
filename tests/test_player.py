import pytest
from talaka_kombat_jrpg.model.player import ButtonCombination, Player, Skill
from tests.conftest import MockSkill


@pytest.fixture
def player(player_1: Player):
    return player_1


def test_player__init():
    player_name = "Tony"
    player = Player(name=player_name)

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


def test_skill__get_combination_length(skill: MockSkill):
    skill.change_combination(
        ButtonCombination(hit_buttons=["P"], move_buttons=["A", "A", "D"])
    )
    assert skill.get_combination_length() == 4

    skill.change_combination(
        ButtonCombination(hit_buttons=["P"], move_buttons=["A", "A", "D", "W", "S"])
    )
    assert skill.get_combination_length() == 6

    skill.change_combination(ButtonCombination(hit_buttons=["P"], move_buttons=[]))
    assert skill.get_combination_length() == 1
