from talaka_kombat_jrpg.player import ButtonCombination, Player, Skill


def test_player__init():
    player_name = "Tony"
    player = Player(player_name=player_name)

    assert player.player_name == player_name
    assert player.energy == 6


def test_player__add_skill():
    new_skill = Skill(
        name="Taladoken",
        cost=1,
        button_combination=ButtonCombination(
            hit_buttons=["P"],
            move_buttons=["A"],
        ),
    )
    player = Player(player_name="Tony")
    player.add_skill(new_skill)

    assert len(player.skills) == 1
    assert player.skills[0].name == "Taladoken"
    assert player.skills[0].cost == 1
    assert player.skills[0].button_combination.hit_button == ["P"]
    assert len(player.skills[0].button_combination.move_buttons) == 1
    assert player.skills[0].button_combination.move_buttons[0] == "A"


def test_player__is_dead():
    player = Player("Player 1")

    assert not player.is_dead()

    player.energy = 0

    assert player.is_dead()


def test_player__is_dead__negative_value():
    player = Player("Player 1")

    assert not player.is_dead()

    player.energy = -2

    assert player.is_dead()
