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
        self.hit_button = hit_buttons
        self.move_buttons = move_buttons


class Skill(ABC):
    def __init__(
        self,
        name: str,
        dammage: int,
        button_combination: ButtonCombination,
    ) -> None:
        self.name = name
        self.dammage = dammage
        self.button_combination = button_combination

    @abstractmethod
    def get_dammage_message(
        self, origin_player: "Player", target_player: "Player"
    ) -> str:
        pass


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
        return self.energy <= 0

    def receive_dammage(self, skill: Skill):
        self.energy -= skill.dammage

    def attack(self, target: "Player", skill: Skill):
        target.receive_dammage(skill)
