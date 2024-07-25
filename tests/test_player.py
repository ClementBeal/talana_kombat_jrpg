from talaka_kombat_jrpg.player import Player, Skill


def test_player__init():
    player_name = "Tony"
    player = Player(player_name=player_name)

    assert player.player_name == player_name
    assert player.energy == 6


def test_player__add_skill():
    player = Player(player_name="Tony")
    player.add_skill(Skill(name="Taladoken"))

    assert len(player.skills) == 1
    assert player.skills[0].name == "Taladoken"
