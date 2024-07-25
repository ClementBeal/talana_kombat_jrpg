from talaka_kombat_jrpg.player import ButtonCombination, Player, Skill


class ArnaldorShuatseneguer(Player):
    def __init__(self) -> None:
        super().__init__("Arnaldor Shuatseneguer")

        self.add_skill(
            Skill(
                name="Remuyuken",
                dammage=3,
                button_combination=ButtonCombination(
                    hit_buttons=["K"], move_buttons=["S", "A"]
                ),
            )
        )
        self.add_skill(
            Skill(
                name="Taladoken",
                dammage=2,
                button_combination=ButtonCombination(
                    hit_buttons=["P"], move_buttons=["A", "S", "A"]
                ),
            )
        )
        self.add_skill(
            Skill(
                name="Patada",
                dammage=1,
                button_combination=ButtonCombination(
                    hit_buttons=["K"], move_buttons=[]
                ),
            )
        )
        self.add_skill(
            Skill(
                name="Puño",
                dammage=1,
                button_combination=ButtonCombination(
                    hit_buttons=["P"], move_buttons=[]
                ),
            )
        )
