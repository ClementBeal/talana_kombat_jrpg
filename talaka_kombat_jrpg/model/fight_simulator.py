from typing import Any
from talaka_kombat_jrpg.model.characters.arnaldor_shuatseneguer import (
    ArnaldorShuatseneguer,
)
from talaka_kombat_jrpg.model.characters.tony_stallone import TonyStallone
from talaka_kombat_jrpg.model.player import Player
from talaka_kombat_jrpg.model.skill_parser import SkillParser


class FightSimulator:
    """

    Example of JSON :
    {
        "player1": {
            "movimientos": [“SDD”, “DSD”, “SA”, “DSD”],
            "golpes": [“K”, “P”, “K”, “P”]
        },
        "player2": {
            "movimientos": [“DSD”, “WSAW”, “ASA”, “”, “ASA”, “SA”],
            "golpes":[“P”, “K”, “K”, “K”, “P”,“k”]
        }
    }
    """

    def __init__(self) -> None:
        self.player_1: Player = TonyStallone()
        self.player_2: Player = ArnaldorShuatseneguer()

    def start_fight(self, fight_data: dict[str, Any]) -> Player:
        """
        Simulates a fight between 2 players

        Returns the winner
        """
        tour = 0
        player_1_is_first = False

        skill_parser = SkillParser()
        skill_parser.parse(fight_data)

        # we don't stop the fight until one of the player is dead
        while not self.player_1.is_dead() and not self.player_2.is_dead():
            # get the actions/skills for each player

            player_1_skill = skill_parser.get_skill(self.player_1, True, tour)
            player_2_skill = skill_parser.get_skill(self.player_2, False, tour)

            if tour == 0:
                # 1. find the first player to attack
                pass

            if player_1_is_first:
                self.player_1.attack(self.player_2, player_1_skill)
                if not self.player_2.is_dead():
                    self.player_2.attack(self.player_1, player_2_skill)
            else:
                self.player_2.attack(self.player_1, player_2_skill)
                if not self.player_1.is_dead():
                    self.player_1.attack(self.player_2, player_1_skill)

            tour += 1

        alive_player = self.player_1 if self.player_2.is_dead() else self.player_2

        print(
            f"{alive_player.player_name} Gana la pelea y aun le queda {alive_player.energy} de energía"
        )

        return alive_player
