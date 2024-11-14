"""
leetcode problem 128
"""


class LongestConsecutive:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1

                longest = max(longest, length)

        return longest
