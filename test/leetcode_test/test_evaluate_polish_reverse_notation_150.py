import pytest
from src.leetcode.evaluate_polish_reverse_notation_150 import (
    EvaluateReversePolishNotation,
)


@pytest.fixture
def rpn_evaluator():
    return EvaluateReversePolishNotation()


def test_simple_addition(rpn_evaluator):
    assert rpn_evaluator.evalRPN(["2", "3", "+"]) == 5


def test_simple_subtraction(rpn_evaluator):
    assert rpn_evaluator.evalRPN(["5", "3", "-"]) == 2


def test_simple_multiplication(rpn_evaluator):
    assert rpn_evaluator.evalRPN(["4", "3", "*"]) == 12


def test_simple_division(rpn_evaluator):
    assert rpn_evaluator.evalRPN(["6", "2", "/"]) == 3


def test_complex_expression(rpn_evaluator):
    assert (
        rpn_evaluator.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    )


def test_negative_numbers(rpn_evaluator):
    assert rpn_evaluator.evalRPN(["-3", "-2", "*", "5", "+"]) == 11


def test_division_rounding(rpn_evaluator):
    assert rpn_evaluator.evalRPN(["14", "-3", "/"]) == -4


def test_single_number(rpn_evaluator):
    assert rpn_evaluator.evalRPN(["18"]) == 18


def test_empty_input(rpn_evaluator):
    with pytest.raises(IndexError):
        rpn_evaluator.evalRPN([])
