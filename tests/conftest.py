import pytest

from talaka_kombat_jrpg.model.player import ButtonCombination, Player, Skill


@pytest.fixture
def player_1_name() -> str:
    return "Tony"


@pytest.fixture
def player_1(player_1_name) -> Player:
    return Player(name=player_1_name)


@pytest.fixture
def player_2_name() -> str:
    return "Arnold"


@pytest.fixture
def player_2(player_2_name):
    return Player(name=player_2_name)


class MockSkill(Skill):
    def __init__(self) -> None:
        super().__init__(
            2,
            ButtonCombination(["K"], ["A", "D"]),
        )

    def change_combination(self, new_combination: ButtonCombination):
        self.button_combination = new_combination

    def get_dammage_message(self, origin_player: Player, target_player: Player) -> str:
        return ""


@pytest.fixture
def skill():
    return MockSkill()


@pytest.fixture
def player_1_with_skill(player_1: Player, skill: Skill):
    player_1.add_skill(skill)
    return player_1
