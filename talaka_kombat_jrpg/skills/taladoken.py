from talaka_kombat_jrpg.player import ButtonCombination, Player, Skill


class Taladoken(Skill):
    def __init__(self, dammage: int, button_combination: ButtonCombination) -> None:
        super().__init__("Taladoken", dammage, button_combination)

    def get_dammage_message(self, origin_player: Player, target_player: Player) -> str:
        return f"{origin_player.player_name} usa un Taladoken"
