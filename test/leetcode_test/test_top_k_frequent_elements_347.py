import pytest
from src.leetcode.top_k_frequent_elements_347 import TopKFrequentElements


def test_basic_case():
    solution = TopKFrequentElements()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert solution.topKFrequent(nums, k) == [1, 2]


def test_single_element():
    solution = TopKFrequentElements()
    nums = [1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]


def test_all_unique_elements():
    solution = TopKFrequentElements()
    nums = [1, 2, 3, 4, 5]
    k = 3
    assert set(solution.topKFrequent(nums, k)) == set([1, 2, 3])


def test_all_same_elements():
    solution = TopKFrequentElements()
    nums = [1, 1, 1, 1, 1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]


def test_negative_numbers():
    solution = TopKFrequentElements()
    nums = [-1, -1, -2, -2, -3, 1, 2, 2]
    k = 3
    assert set(solution.topKFrequent(nums, k)) == set([-1, -2, 2])


def test_k_equals_length():
    solution = TopKFrequentElements()
    nums = [1, 2, 3, 4]
    k = 4
    assert set(solution.topKFrequent(nums, k)) == set([1, 2, 3, 4])


def test_empty_list():
    solution = TopKFrequentElements()
    nums = []
    k = 0
    assert solution.topKFrequent(nums, k) == []


def test_large_input():
    solution = TopKFrequentElements()
    nums = [i % 100 for i in range(10000)]  # 0-99 repeated 100 times each
    k = 50
    result = solution.topKFrequent(nums, k)
    assert len(result) == k
    assert set(result) == set(range(50))  # All numbers from 0-49 should be
