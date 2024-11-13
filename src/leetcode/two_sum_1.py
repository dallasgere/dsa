"""
leetcode problem 1
"""


class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """determines if there are two numbers that add up to meet target in o(n)

        Args:
            nums (list[int]): the list of numbers to search through
            target (int): the target we are trying to add to

        Returns:
            list[int]: empty if not available two sums, unordered list if it is
        """
        prev = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in prev:
                return [prev[diff], i]

            prev[val] = i

        return []
