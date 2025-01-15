import pytest
from src.leetcode.search_in_rotated_sorted_array_33 import SearchInRotatedSortedArray


@pytest.fixture
def search_instance():
    return SearchInRotatedSortedArray()


def test_search_in_rotated_sorted_array_target_present(search_instance):
    assert search_instance.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert (
        search_instance.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
    )
    assert search_instance.search_in_rotated_sorted_array([1], 0) == -1
    assert search_instance.search_in_rotated_sorted_array([1], 1) == 0


def test_search_in_rotated_sorted_array_edge_cases(search_instance):
    assert search_instance.search_in_rotated_sorted_array([], 5) == -1
    assert search_instance.search_in_rotated_sorted_array([1, 3], 3) == 1


def test_search_in_rotated_sorted_array_rotated(search_instance):
    assert search_instance.search_in_rotated_sorted_array([3, 1], 1) == 1
    assert search_instance.search_in_rotated_sorted_array([5, 1, 3], 5) == 0


def test_search_in_rotated_sorted_array_not_rotated(search_instance):
    assert search_instance.search_in_rotated_sorted_array([1, 2, 3, 4, 5], 3) == 2
    assert search_instance.search_in_rotated_sorted_array([1, 2, 3, 4, 5], 6) == -1
