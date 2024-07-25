import json
from typing import Any

from talaka_kombat_jrpg.model.player import Player, Skill
from talaka_kombat_jrpg.model.skills.move import Move


class SkillParser:
    """
    Part of the fight simulator that parse the inputs (moves + hit) of each player and that find the skill associated to this action
    """

    def parse(self, fight_data: str) -> None:
        self.fight_data: dict[str, Any] = json.loads(fight_data)

    def get_skill(self, player: Player, is_player_1: bool, tour: int) -> Skill:
        player_key = "player1" if is_player_1 else "player2"

        current_moves = self.fight_data[player_key]["movimientos"][tour]
        current_hit = self.fight_data[player_key]["golpes"][tour]

        if current_hit == "":
            return Move()

        for skill in player.skills:
            if skill.button_combination.matches_string(current_hit, current_moves):
                return skill

        raise NotImplementedError()
