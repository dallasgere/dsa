import pytest
from src.leetcode.longest_consecutive_sequence_128 import LongestConsecutive


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),  # Normal case
        ([0, 1, 2, 3, 4, 5], 6),  # Consecutive numbers
        ([10, 9, 8, 7], 4),  # Descending consecutive numbers
        ([], 0),  # Empty list
        ([1], 1),  # Single element
        ([1, 2, 0, 1], 3),  # Duplicate elements
    ],
)
def test_longest_consecutive(nums, expected):
    lc = LongestConsecutive()
    assert lc.longestConsecutive(nums) == expected
