from typing import Any

from talaka_kombat_jrpg.model.player import Player, Skill
from talaka_kombat_jrpg.model.skills.move import Move


class SkillParser:
    """
    Part of the fight simulator that parse the inputs (moves + hit) of each player and that find the skill associated to this action
    """

    def __init__(self, fight_data: dict[str, Any]) -> None:
        self.fight_data: dict[str, Any] = fight_data

    def get_skills(self, player: Player, is_player_1: bool, tour: int) -> list[Skill]:
        """
        Find the list of skills/actions to do from the data for a specific round of the game

        Args:
            player: a Player
            is_player_1: true if we search into the player 1 skills otherwise false
            tour: the current tour/round of the simulation
        """
        player_key = "player1" if is_player_1 else "player2"

        if len(self.fight_data[player_key]["movimientos"]) <= tour:
            return []

        current_moves = self.fight_data[player_key]["movimientos"][tour]
        current_hit = self.fight_data[player_key]["golpes"][tour]

        skills: list[Skill] = []
        index: int = 0

        # if we don't have moves, it means the user is using the hit buttons
        if current_moves == "":
            for skill in player.skills:
                if skill.button_combination.matches_string(current_hit, ""):
                    # we can only have one hit/golpe each turn
                    return [skill]

        # the specs say that the player only have moves actions until he attacks
        # we check if buttons match a skill of the player
        # if yes, we add the skill to the skill list and we're done here
        # if no, we add a Move to the list and we increase the index by 1
        # so we can continue to search a skill of type "attack"
        while index < len(current_moves):
            for skill in player.skills:
                if skill.button_combination.matches_string(
                    current_hit, current_moves[index:]
                ):
                    # it means we have a combination and it's always the last move of a sequence
                    # that's why we return all the skills
                    skills.append(skill)
                    return skills

            skills.append(Move(current_moves[index]))
            index += 1

        # sometimes the player only moves and doesn't use a combo
        # in this case, we probably have a hit with "K" or "P"
        for skill in player.skills:
            if skill.button_combination.matches_string(current_hit, ""):
                # we can only have one hit/golpe each turn
                skills.append(skill)

        return skills
