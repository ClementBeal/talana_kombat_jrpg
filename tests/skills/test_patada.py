from talaka_kombat_jrpg.model.player import ButtonCombination
from talaka_kombat_jrpg.model.skills.patada import Patada


def test_patadata__get_dammage_message(player_1, player_2, player_1_name):
    skill = Patada(3, ButtonCombination([], []))
    assert (
        skill.get_dammage_message(player_1, player_2)
        == f"{player_1_name} avanza y da una patada"
    )
