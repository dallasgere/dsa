import pytest
from src.leetcode.contains_duplicate_217 import ContainsDuplicate


@pytest.fixture
def solution():
    return ContainsDuplicate()


def test_contains_duplicate_with_duplicates(solution):
    assert solution.containsDuplicate([1, 2, 3, 1]) == True


def test_contains_duplicate_without_duplicates(solution):
    assert solution.containsDuplicate([1, 2, 3, 4]) == False


def test_contains_duplicate_empty_list(solution):
    assert solution.containsDuplicate([]) == False


def test_contains_duplicate_single_element(solution):
    assert solution.containsDuplicate([1]) == False


def test_contains_duplicate_all_same_elements(solution):
    assert solution.containsDuplicate([2, 2, 2, 2]) == True


def test_contains_duplicate_large_list_with_duplicate(solution):
    large_list = list(range(1000000)) + [42, 42]
    assert solution.containsDuplicate(large_list) == True


def test_contains_duplicate_negative_numbers(solution):
    assert solution.containsDuplicate([-1, -2, -3, -1]) == True


def test_contains_duplicate_mixed_numbers(solution):
    assert solution.containsDuplicate([-1, 0, 1, 2, -1]) == True
