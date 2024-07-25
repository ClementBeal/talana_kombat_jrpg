from talaka_kombat_jrpg.model.player import ButtonCombination, Player
from talaka_kombat_jrpg.model.skills.patada import Patada
from talaka_kombat_jrpg.model.skills.puno import Puno
from talaka_kombat_jrpg.model.skills.remuyuken import Remuyuken
from talaka_kombat_jrpg.model.skills.taladoken import Taladoken


class ArnaldorShuatseneguer(Player):
    def __init__(self) -> None:
        super().__init__("Arnaldor Shuatseneguer")

        self.add_skill(
            Remuyuken(
                3,
                button_combination=ButtonCombination(
                    hit_buttons=["K"], move_buttons=["S", "A"]
                ),
            ),
        )
        self.add_skill(
            Taladoken(
                2,
                button_combination=ButtonCombination(
                    hit_buttons=["P"], move_buttons=["A", "S", "A"]
                ),
            ),
        )
        self.add_skill(
            Patada(
                1,
                button_combination=ButtonCombination(
                    hit_buttons=["K"], move_buttons=[]
                ),
            )
        )
        self.add_skill(
            Puno(
                1,
                button_combination=ButtonCombination(
                    hit_buttons=["P"], move_buttons=[]
                ),
            )
        )
