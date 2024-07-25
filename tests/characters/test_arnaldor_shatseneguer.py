from talaka_kombat_jrpg.model.characters.arnaldor_shuatseneguer import (
    ArnaldorShuatseneguer,
)
from talaka_kombat_jrpg.model.skills.patada import Patada
from talaka_kombat_jrpg.model.skills.puno import Puno
from talaka_kombat_jrpg.model.skills.remuyuken import Remuyuken
from talaka_kombat_jrpg.model.skills.taladoken import Taladoken


def test_arnaldor_shatseneguer__init():
    arnaldor_shatseneguer = ArnaldorShuatseneguer()

    assert arnaldor_shatseneguer.player_name == "Arnaldor Shuatseneguer"
    assert arnaldor_shatseneguer.energy == 6
    assert len(arnaldor_shatseneguer.skills) == 4

    remuyuken = arnaldor_shatseneguer.skills[0]
    taladoken = arnaldor_shatseneguer.skills[1]
    patada = arnaldor_shatseneguer.skills[2]
    puno = arnaldor_shatseneguer.skills[3]

    assert isinstance(remuyuken, Remuyuken)
    assert isinstance(taladoken, Taladoken)
    assert isinstance(patada, Patada)
    assert isinstance(puno, Puno)

    assert remuyuken.dammage == 3
    assert taladoken.dammage == 2
    assert patada.dammage == 1
    assert puno.dammage == 1

    assert remuyuken.button_combination.hit_buttons[0] == "K"
    assert taladoken.button_combination.hit_buttons[0] == "P"
    assert patada.button_combination.hit_buttons[0] == "K"
    assert puno.button_combination.hit_buttons[0] == "P"

    assert remuyuken.button_combination.move_buttons == ["S", "A"]
    assert taladoken.button_combination.move_buttons == [
        "A",
        "S",
        "A",
    ]
    assert patada.button_combination.move_buttons == []
    assert puno.button_combination.move_buttons == []
