from talaka_kombat_jrpg.player import ButtonCombination, Player, Skill


class TonyStallone(Player):
    def __init__(self) -> None:
        super().__init__("Tony Stallone")

        self.add_skill(
            Skill(
                name="Taladoken",
                dammage=3,
                button_combination=ButtonCombination(
                    hit_buttons=["P"], move_buttons=["D", "S", "D"]
                ),
            )
        )
        self.add_skill(
            Skill(
                name="Remuyuken",
                dammage=2,
                button_combination=ButtonCombination(
                    hit_buttons=["K"], move_buttons=["S", "D"]
                ),
            )
        )
        self.add_skill(
            Skill(
                name="Patada",
                dammage=1,
                button_combination=ButtonCombination(
                    hit_buttons=["P", "K"], move_buttons=[]
                ),
            )
        )
