from talaka_kombat_jrpg.characters.arnaldor_shuatseneguer import ArnaldorShuatseneguer


def test_arnaldor_shatseneguer__init():
    arnaldor_shatseneguer = ArnaldorShuatseneguer()

    assert arnaldor_shatseneguer.player_name == "Arnaldor Shuatseneguer"
    assert arnaldor_shatseneguer.energy == 6
    assert len(arnaldor_shatseneguer.skills) == 3

    assert arnaldor_shatseneguer.skills[0].name == "Remuyuken"
    assert arnaldor_shatseneguer.skills[1].name == "Taladoken"
    assert arnaldor_shatseneguer.skills[2].name == "Patada"

    assert arnaldor_shatseneguer.skills[0].dammage == 3
    assert arnaldor_shatseneguer.skills[1].dammage == 2
    assert arnaldor_shatseneguer.skills[2].dammage == 1

    assert arnaldor_shatseneguer.skills[0].button_combination.hit_button[0] == "K"
    assert arnaldor_shatseneguer.skills[1].button_combination.hit_button[0] == "P"
    assert "P" in arnaldor_shatseneguer.skills[2].button_combination.hit_button
    assert "K" in arnaldor_shatseneguer.skills[2].button_combination.hit_button

    assert arnaldor_shatseneguer.skills[0].button_combination.move_buttons == ["S", "A"]
    assert arnaldor_shatseneguer.skills[1].button_combination.move_buttons == [
        "A",
        "S",
        "A",
    ]
    assert arnaldor_shatseneguer.skills[2].button_combination.move_buttons == []
