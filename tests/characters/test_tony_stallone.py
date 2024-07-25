from talaka_kombat_jrpg.characters.tony_stallone import TonyStallone


def test_tony_stallone__init():
    tony_stallone = TonyStallone()

    assert tony_stallone.player_name == "Tony Stallone"
    assert tony_stallone.energy == 6
    assert len(tony_stallone.skills) == 3

    assert tony_stallone.skills[0].name == "Taladoken"
    assert tony_stallone.skills[1].name == "Remuyuken"
    assert tony_stallone.skills[2].name == "Patada"

    assert tony_stallone.skills[0].dammage == 3
    assert tony_stallone.skills[1].dammage == 2
    assert tony_stallone.skills[2].dammage == 1

    assert tony_stallone.skills[0].button_combination.hit_button[0] == "P"
    assert tony_stallone.skills[1].button_combination.hit_button[0] == "K"
    assert "P" in tony_stallone.skills[2].button_combination.hit_button
    assert "K" in tony_stallone.skills[2].button_combination.hit_button

    assert tony_stallone.skills[0].button_combination.move_buttons == ["D", "S", "D"]
    assert tony_stallone.skills[1].button_combination.move_buttons == ["S", "D"]
    assert tony_stallone.skills[2].button_combination.move_buttons == []
