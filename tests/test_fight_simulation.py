from talaka_kombat_jrpg.model.fight_simulator import FightSimulator


def test_fight_simulator():
    fight_data = {
        "player1": {
            "movimientos": ["D", "DSD", "S", "DSD", "SD"],
            "golpes": ["K", "P", "", "K", "P"],
        },
        "player2": {
            "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
            "golpes": ["K", "", "K", "P", "P"],
        },
    }

    simulator = FightSimulator()
    winner = simulator.start_fight(fight_data)

    assert winner is simulator.player_2
    assert winner.energy == 2
