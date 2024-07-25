from talaka_kombat_jrpg.player import ButtonCombination
from talaka_kombat_jrpg.skills.remuyuken import Remuyuken


def test_remuyuken__get_dammage_message(player_1, player_2, player_1_name):
    skill = Remuyuken(3, ButtonCombination([], []))
    assert (
        skill.get_dammage_message(player_1, player_2)
        == f"{player_1_name} conecta un Remuyuken"
    )
