import pytest
from talaka_kombat_jrpg.player import ButtonCombination, Player, Skill


@pytest.fixture
def player():
    return Player("Player 1")


@pytest.fixture
def skill():
    return Skill(
        "Skill 1",
        dammage=2,
        button_combination=ButtonCombination(
            [],
            [],
        ),
    )


def test_player__init():
    player_name = "Tony"
    player = Player(player_name=player_name)

    assert player.player_name == player_name
    assert player.energy == 6


def test_player__add_skill(player: Player):
    new_skill = Skill(
        name="Taladoken",
        dammage=1,
        button_combination=ButtonCombination(
            hit_buttons=["P"],
            move_buttons=["A"],
        ),
    )
    player.add_skill(new_skill)

    assert len(player.skills) == 1
    assert player.skills[0].name == "Taladoken"
    assert player.skills[0].dammage == 1
    assert player.skills[0].button_combination.hit_button == ["P"]
    assert len(player.skills[0].button_combination.move_buttons) == 1
    assert player.skills[0].button_combination.move_buttons[0] == "A"


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
