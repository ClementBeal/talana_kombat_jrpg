from typing import Any
from talaka_kombat_jrpg.model.characters.arnaldor_shuatseneguer import (
    ArnaldorShuatseneguer,
)
from talaka_kombat_jrpg.model.characters.tony_stallone import TonyStallone
from talaka_kombat_jrpg.model.player import Player, Skill
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
        player_1_is_first = True

        skill_parser = SkillParser()
        skill_parser.parse(fight_data)

        # we don't stop the fight until one of the player is dead
        while not self.player_1.is_dead() and not self.player_2.is_dead():
            # get the actions/skills for each player
            player_1_skill = skill_parser.get_skills(self.player_1, True, tour)
            player_2_skill = skill_parser.get_skills(self.player_2, False, tour)

            if tour == 0:
                pass
                # player_1_skill_len = player_1_skill.get_combination_length()
                # player_2_skill_len = player_2_skill.get_combination_length()
                # player_1_is_first = player_1_skill_len <= player_2_skill_len

            if player_1_is_first:
                self._player_attack(self.player_1, self.player_2, player_1_skill)
                if not self.player_2.is_dead():
                    self._player_attack(self.player_2, self.player_1, player_2_skill)
            else:
                self._player_attack(self.player_2, self.player_1, player_2_skill)
                if not self.player_1.is_dead():
                    self._player_attack(self.player_1, self.player_2, player_1_skill)

            tour += 1

        alive_player = self.player_1 if self.player_2.is_dead() else self.player_2

        print(
            f"{alive_player.player_name} Gana la pelea y aun le queda {alive_player.energy} de energía"
        )

        return alive_player

    def _player_attack(
        self, origin_player: Player, target_player: Player, skills: list[Skill]
    ):
        for skill in skills:
            origin_player.attack(target_player, skill)
