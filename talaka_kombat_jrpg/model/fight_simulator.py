from dataclasses import dataclass
from typing import Any
from talaka_kombat_jrpg.model.characters.arnaldor_shuatseneguer import (
    ArnaldorShuatseneguer,
)
from talaka_kombat_jrpg.model.characters.tony_stallone import TonyStallone
from talaka_kombat_jrpg.model.player import Player, Skill
from talaka_kombat_jrpg.model.skill_parser import SkillParser


@dataclass
class FightResult:
    winner: Player
    history: str


class FightSimulator:
    """
    Simulate a fight between 2 players pre defined.
    The simulator receive a JSON with the format defined below. Those data are parsed to execute action between the players.

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

    def start_fight(self, fight_data: dict[str, Any]) -> FightResult:
        """
        Simulates a fight between 2 players using fight data.

        Returns a fight result
        """
        tour = 0
        player_1_is_first = True
        history: list[str] = []

        skill_parser = SkillParser(fight_data)

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
                history.extend(
                    self._player_attack(self.player_1, self.player_2, player_1_skill)
                )
                if not self.player_2.is_dead():
                    history.extend(
                        self._player_attack(
                            self.player_2, self.player_1, player_2_skill
                        )
                    )
            else:
                history.extend(
                    self._player_attack(self.player_2, self.player_1, player_2_skill)
                )
                if not self.player_1.is_dead():
                    history.extend(
                        self._player_attack(
                            self.player_1, self.player_2, player_1_skill
                        )
                    )

            tour += 1

        winner = self.player_1 if self.player_2.is_dead() else self.player_2

        history.append(
            f"{winner.player_name} Gana la pelea y aun le queda {winner.energy} de energía"
        )

        return FightResult(winner, "\n".join(history))

    def _player_attack(
        self, origin_player: Player, target_player: Player, skills: list[Skill]
    ) -> list[str]:
        history: list[str] = []

        for skill in skills:
            action_result = origin_player.attack(target_player, skill)
            history.append(action_result)

        return history
