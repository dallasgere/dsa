"""leetcode problem 153: find minimum in rotated sorted array

link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""


class FindMinimumInRotatedSortedArray:
    def find_min(self, nums: list[int]) -> int:
        """Find min value in rotated sorted array.

        Uses binary search to be super fast.

        Args:
            nums (list[int]): the rotated sorted array to search through

        Returns:
            int: the min value in the rotated sorted array
        """

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        return nums[l]
