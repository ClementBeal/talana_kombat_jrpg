from talaka_kombat_jrpg.model.player import ButtonCombination
from talaka_kombat_jrpg.model.skills.puno import Puno


def test_puno__get_dammage_message(player_1, player_2, player_1_name, player_2_name):
    skill = Puno(3, ButtonCombination([], []))
    assert (
        skill.get_dammage_message(player_1, player_2)
        == f"{player_1_name} le da un puñetazo al pobre {player_2_name}"
    )
