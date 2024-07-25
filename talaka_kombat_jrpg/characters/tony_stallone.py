from talaka_kombat_jrpg.player import ButtonCombination, Player
from talaka_kombat_jrpg.skills.patada import Patada
from talaka_kombat_jrpg.skills.puno import Puno
from talaka_kombat_jrpg.skills.remuyuken import Remuyuken
from talaka_kombat_jrpg.skills.taladoken import Taladoken


class TonyStallone(Player):
    def __init__(self) -> None:
        super().__init__("Tony Stallone")

        self.add_skill(
            Taladoken(
                dammage=3,
                button_combination=ButtonCombination(
                    hit_buttons=["P"], move_buttons=["D", "S", "D"]
                ),
            )
        )
        self.add_skill(
            Remuyuken(
                dammage=2,
                button_combination=ButtonCombination(
                    hit_buttons=["K"], move_buttons=["S", "D"]
                ),
            )
        )
        self.add_skill(
            Patada(
                dammage=1,
                button_combination=ButtonCombination(
                    hit_buttons=["K"], move_buttons=[]
                ),
            )
        )
        self.add_skill(
            Puno(
                dammage=1,
                button_combination=ButtonCombination(
                    hit_buttons=["P"], move_buttons=[]
                ),
            )
        )
