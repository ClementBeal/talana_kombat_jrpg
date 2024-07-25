class ButtonCombination:
    def __init__(self, hit_button: str, move_buttons: str) -> None:
        self.hit_button = hit_button
        self.move_buttons = move_buttons


class Skill:
    def __init__(
        self,
        name: str,
        cost: int,
        button_combination: ButtonCombination,
    ) -> None:
        self.name = name
        self.cost = cost
        self.button_combination = button_combination


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
