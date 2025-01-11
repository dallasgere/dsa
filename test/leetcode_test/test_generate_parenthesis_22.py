import pytest
from src.leetcode.generate_parenthesis_22 import GenerateParenthesis


@pytest.fixture
def generate_parenthesis():
    return GenerateParenthesis()


def test_generate_parenthesis_n_1(generate_parenthesis):
    assert generate_parenthesis.generateParenthesis(1) == ["()"]


def test_generate_parenthesis_n_2(generate_parenthesis):
    assert set(generate_parenthesis.generateParenthesis(2)) == set(["(())", "()()"])


def test_generate_parenthesis_n_3(generate_parenthesis):
    expected = set(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert set(generate_parenthesis.generateParenthesis(3)) == expected


def test_generate_parenthesis_length(generate_parenthesis):
    n = 4
    result = generate_parenthesis.generateParenthesis(n)
    assert all(len(s) == 2 * n for s in result)


def test_generate_parenthesis_valid(generate_parenthesis):
    def is_valid(s):
        count = 0
        for char in s:
            if char == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    n = 5
    result = generate_parenthesis.generateParenthesis(n)
    assert all(is_valid(s) for s in result)


def test_generate_parenthesis_unique(generate_parenthesis):
    n = 6
    result = generate_parenthesis.generateParenthesis(n)
    assert len(result) == len(set(result))
