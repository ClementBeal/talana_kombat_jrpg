from talaka_kombat_jrpg.model.player import ButtonCombination
from talaka_kombat_jrpg.model.skills.taladoken import Taladoken


def test_taladoken__get_dammage_message(player_1, player_2, player_1_name):
    skill = Taladoken(3, ButtonCombination([], []))
    assert (
        skill.get_dammage_message(player_1, player_2)
        == f"{player_1_name} usa un Taladoken"
    )
