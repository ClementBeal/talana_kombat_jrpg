from talaka_kombat_jrpg.model.player import ButtonCombination, Player, Skill


class Move(Skill):
    def __init__(self, direction: str) -> None:
        super().__init__(0, ButtonCombination([], []))

        self.direction = direction

    def get_dammage_message(self, origin_player: Player, target_player: Player) -> str:
        direction_str = ""
        match self.direction:
            case "A":
                direction_str = "atras"
            case "W":
                direction_str = "arriba"
            case "S":
                direction_str = "abajo"
            case "D":
                direction_str = "adelante"

        return f"{origin_player.player_name} se mueve {direction_str}"
