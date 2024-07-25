from talaka_kombat_jrpg.model.skills.move import Move


def test_move__get_dammage_message(player_1, player_2, player_1_name):
    skill = Move(direction="A")
    assert (
        skill.get_dammage_message(player_1, player_2)
        == f"{player_1_name} se mueve atras"
    )
