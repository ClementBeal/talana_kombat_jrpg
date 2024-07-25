import pytest
from talaka_kombat_jrpg.player import ButtonCombination, Player
from talaka_kombat_jrpg.skill_parser import SkillParser
from talaka_kombat_jrpg.skills.move import Move
from tests.conftest import MockSkill


@pytest.fixture
def skill_parser():
    return SkillParser()


def test_skill_parser__only_moves(
    skill_parser: SkillParser, player_1_with_skill: Player
):
    skill_parser.parse(
        """{
            "player1": {"movimientos": ["A", "S"], "golpes": [""]},
            "player2": {"movimientos": [], "golpes": []}
        }"""
    )

    skill = skill_parser.get_skill(player_1_with_skill, True, 0)

    assert isinstance(skill, Move)


def test_skill_parser__only_hit(
    skill_parser: SkillParser, player_1: Player, skill: MockSkill
):
    skill.change_combination(ButtonCombination(["P"], []))
    player_1.add_skill(skill)

    skill_parser.parse(
        """{
            "player1": {"movimientos": [""], "golpes": ["P"]},
            "player2": {"movimientos": [""], "golpes": [""]}
        }"""
    )

    parsed_skill = skill_parser.get_skill(player_1, True, 0)

    assert parsed_skill is skill
