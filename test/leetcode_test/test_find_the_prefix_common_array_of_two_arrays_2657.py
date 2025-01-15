import pytest
from src.leetcode.find_the_prefix_common_array_of_two_arrays_2657 import (
    FindThePrefixCommonArrayOfTwoArrays,
)


@pytest.fixture
def prefix_common_array():
    return FindThePrefixCommonArrayOfTwoArrays()


def test_empty_arrays(prefix_common_array):
    assert prefix_common_array.solution([], []) == []


def test_single_element_arrays(prefix_common_array):
    assert prefix_common_array.solution([1], [1]) == [1]
    assert prefix_common_array.solution([1], [2]) == [0]


def test_small_arrays(prefix_common_array):
    assert prefix_common_array.solution([1, 2, 3], [2, 1, 3]) == [0, 2, 3]
    assert prefix_common_array.solution([1, 2, 3], [3, 2, 1]) == [0, 1, 3]


def test_larger_arrays(prefix_common_array):
    assert prefix_common_array.solution([1, 2, 3, 4, 5], [3, 1, 2, 5, 4]) == [
        0,
        1,
        3,
        3,
        5,
    ]


def test_no_common_elements(prefix_common_array):
    assert prefix_common_array.solution([1, 2, 3, 4], [5, 6, 7, 8]) == [0, 0, 0, 0]


def test_all_common_elements(prefix_common_array):
    assert prefix_common_array.solution([1, 2, 3, 4], [1, 2, 3, 4]) == [1, 2, 3, 4]


def test_count_common_method(prefix_common_array):
    assert prefix_common_array.count_common({1, 2, 3}, {2, 3, 4}) == 2
    assert prefix_common_array.count_common({1, 2, 3}, {4, 5, 6}) == 0
    assert prefix_common_array.count_common({1, 2, 3}, {1, 2, 3}) == 3
