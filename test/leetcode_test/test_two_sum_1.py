import pytest
from src.leetcode.two_sum_1 import TwoSum


@pytest.fixture
def solution():
    return TwoSum()


def test_two_sum_found(solution):
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]


def test_two_sum_not_found(solution):
    assert solution.twoSum([1, 2, 3], 7) == []
    assert solution.twoSum([], 0) == []
    assert solution.twoSum([1], 1) == []


def test_two_sum_negative_numbers(solution):
    assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_two_sum_with_duplicates(solution):
    assert solution.twoSum([1, 5, 5, 11], 10) == [1, 2]
    assert solution.twoSum([0, 4, 3, 0], 0) == [0, 3]
