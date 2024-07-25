from talaka_kombat_jrpg.player import Player


def test_player__init():
    player_name = "Tony"
    player = Player(player_name=player_name)

    assert player.player_name == player_name
    assert player.energy == 6
