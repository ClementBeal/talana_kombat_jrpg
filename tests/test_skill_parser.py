import pytest
from talaka_kombat_jrpg.model.player import ButtonCombination, Player
from talaka_kombat_jrpg.model.skill_parser import SkillParser
from talaka_kombat_jrpg.model.skills.move import Move
from tests.conftest import MockSkill


@pytest.fixture
def skill_parser():
    return SkillParser()


def test_skill_parser__only_moves(
    skill_parser: SkillParser, player_1_with_skill: Player
):
    skill_parser.parse(
        {
            "player1": {"movimientos": ["AS"], "golpes": [""]},
            "player2": {"movimientos": [], "golpes": []},
        }
    )

    skills = skill_parser.get_skills(player_1_with_skill, True, 0)

    assert len(skills) == 2
    assert all([isinstance(skill, Move) for skill in skills])


def test_skill_parser__only_hit(
    skill_parser: SkillParser, player_1: Player, skill: MockSkill
):
    skill.change_combination(ButtonCombination(["P"], []))
    player_1.add_skill(skill)

    skill_parser.parse(
        {
            "player1": {"movimientos": [""], "golpes": ["P"]},
            "player2": {"movimientos": [""], "golpes": [""]},
        }
    )

    parsed_skills = skill_parser.get_skills(player_1, True, 0)

    assert len(parsed_skills) == 1
    assert parsed_skills[0] is skill
