from abc import ABC, abstractmethod
from typing import Literal


class ButtonCombination:
    """
    The simplest way to define a combination of buttons for a skill

    hit_button: a list of "P" or "K"
    move_buttons: a list of moves buttons. Either "A", "W", "S", "D"
    """

    def __init__(
        self,
        hit_buttons: list[Literal["P", "K"]],
        move_buttons: list[Literal["A", "W", "S", "D"]],
    ) -> None:
        self.hit_buttons = hit_buttons
        self.move_buttons = move_buttons

    def matches_string(self, hits: str, moves: str) -> bool:
        return "".join(self.hit_buttons) == hits and "".join(self.move_buttons) == moves


class Skill(ABC):
    def __init__(
        self,
        dammage: int,
        button_combination: ButtonCombination,
    ) -> None:
        self.dammage = dammage
        self.button_combination = button_combination

    @abstractmethod
    def get_dammage_message(
        self, origin_player: "Player", target_player: "Player"
    ) -> str:
        """
        Returns a message to describe the action that occurs during the game/fight

        args:
            origin_player: the player who used the skill.
            target_player: the player who is the target of the skill.
        """
        pass

    def matchs_combination(self, combination: ButtonCombination) -> bool:
        return self.button_combination == combination


class Player:
    def __init__(
        self,
        player_name: str,
        energy: int = 6,
    ) -> None:
        self.player_name = player_name
        self.energy = energy
        self.skills: list[Skill] = []

    def add_skill(self, new_skill: Skill):
        self.skills.append(new_skill)

    def is_dead(self) -> bool:
        """
        Checks if the player is dead or not

        returns True if the player is dead else false
        """
        return self.energy <= 0

    def receive_dammage(self, skill: Skill):
        """
        Substracts thr skill's dammage to the current energy
        """
        self.energy -= skill.dammage

    def attack(self, target: "Player", skill: Skill):
        """
        Attacks a player with a specific skill
        """
        target.receive_dammage(skill)
