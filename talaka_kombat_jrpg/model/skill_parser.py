from typing import Any

from talaka_kombat_jrpg.model.player import Player, Skill
from talaka_kombat_jrpg.model.skills.move import Move


class SkillParser:
    """
    Part of the fight simulator that parse the inputs (moves + hit) of each player and that find the skill associated to this action
    """

    def parse(self, fight_data: dict[str, Any]) -> None:
        self.fight_data: dict[str, Any] = fight_data

    def get_skills(self, player: Player, is_player_1: bool, tour: int) -> list[Skill]:
        player_key = "player1" if is_player_1 else "player2"

        current_moves = self.fight_data[player_key]["movimientos"][tour]
        current_hit = self.fight_data[player_key]["golpes"][tour]

        if current_hit == "":
            print(current_moves)
            return [Move(direction) for direction in current_moves]

        for skill in player.skills:
            if skill.button_combination.matches_string(current_hit, current_moves):
                return [skill]

        raise NotImplementedError()
