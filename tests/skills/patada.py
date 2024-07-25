from talaka_kombat_jrpg.model.player import ButtonCombination, Player, Skill


class Patada(Skill):
    def __init__(self, dammage: int, button_combination: ButtonCombination) -> None:
        super().__init__(dammage, button_combination)

    def get_dammage_message(self, origin_player: Player, target_player: Player) -> str:
        return f"{origin_player.player_name} Arnardold Gana la pelea y aun le queda {target_player.energy} de energía"
