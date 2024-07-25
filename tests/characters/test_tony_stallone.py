from talaka_kombat_jrpg.characters.tony_stallone import TonyStallone
from talaka_kombat_jrpg.skills.patada import Patada
from talaka_kombat_jrpg.skills.puno import Puno
from talaka_kombat_jrpg.skills.remuyuken import Remuyuken
from talaka_kombat_jrpg.skills.taladoken import Taladoken


def test_tony_stallone__init():
    tony_stallone = TonyStallone()

    assert tony_stallone.player_name == "Tony Stallone"
    assert tony_stallone.energy == 6
    assert len(tony_stallone.skills) == 4

    remuyuken = tony_stallone.skills[0]
    taladoken = tony_stallone.skills[1]
    patada = tony_stallone.skills[2]
    puno = tony_stallone.skills[3]

    assert isinstance(remuyuken, Taladoken)
    assert isinstance(taladoken, Remuyuken)
    assert isinstance(patada, Patada)
    assert isinstance(puno, Puno)

    assert remuyuken.dammage == 3
    assert taladoken.dammage == 2
    assert patada.dammage == 1
    assert puno.dammage == 1

    assert remuyuken.button_combination.hit_button[0] == "P"
    assert taladoken.button_combination.hit_button[0] == "K"
    assert patada.button_combination.hit_button[0] == "K"
    assert puno.button_combination.hit_button[0] == "P"

    assert remuyuken.button_combination.move_buttons == ["D", "S", "D"]
    assert taladoken.button_combination.move_buttons == ["S", "D"]
    assert patada.button_combination.move_buttons == []
    assert puno.button_combination.move_buttons == []
