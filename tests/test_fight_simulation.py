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
    result = simulator.start_fight(fight_data)
    winner = result.winner

    assert winner is simulator.player_2
    assert winner.energy == 2
    assert simulator.player_1.energy == 0


def test_fight_simulator__two():
    fight_data = {
        "player1": {"movimientos": ["DSD", "S"], "golpes": ["P", ""]},
        "player2": {
            "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
            "golpes": ["P", "", "P", "K", "K", "K"],
        },
    }

    simulator = FightSimulator()
    result = simulator.start_fight(fight_data)
    winner = result.winner

    assert winner is simulator.player_2
    assert winner.energy == 3
    assert simulator.player_1.energy == -1


def test_fight_simulator__three():
    fight_data = {
        "player1": {
            "movimientos": ["SDD", "DSD", "SA", "DSD"],
            "golpes": ["K", "P", "K", "P"],
        },
        "player2": {
            "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
            "golpes": ["P", "K", "K", "K", "P", "k"],
        },
    }

    simulator = FightSimulator()
    result = simulator.start_fight(fight_data)
    winner = result.winner

    assert winner is simulator.player_1
    assert winner.energy == 1
    assert simulator.player_2.energy == -2
