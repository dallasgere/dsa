import pytest
from src.leetcode.find_minimum_in_rotated_sorted_array_153 import (
    FindMinimumInRotatedSortedArray,
)


@pytest.fixture
def solution():
    return FindMinimumInRotatedSortedArray()


def test_find_min_rotated_array(solution):
    assert solution.find_min([3, 4, 5, 1, 2]) == 1
    assert solution.find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.find_min([11, 13, 15, 17]) == 11


def test_find_min_single_element(solution):
    assert solution.find_min([1]) == 1


def test_find_min_two_elements(solution):
    assert solution.find_min([2, 1]) == 1
    assert solution.find_min([1, 2]) == 1


def test_find_min_not_rotated(solution):
    assert solution.find_min([1, 2, 3, 4, 5]) == 1


def test_find_min_negative_numbers(solution):
    assert solution.find_min([-3, -2, -1, 0, -5, -4]) == -5


def test_find_min_all_negative(solution):
    assert solution.find_min([-3, -2, -1, -5, -4]) == -5
