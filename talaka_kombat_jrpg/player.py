class Skill:
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
        pass
