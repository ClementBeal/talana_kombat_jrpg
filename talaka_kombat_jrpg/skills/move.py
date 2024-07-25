from talaka_kombat_jrpg.player import ButtonCombination, Player, Skill


class Move(Skill):
    def __init__(self) -> None:
        super().__init__(0, ButtonCombination([], []))

    def get_dammage_message(self, origin_player: Player, target_player: Player) -> str:
        return f"{origin_player.player_name} se mueve"
