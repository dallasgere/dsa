"""leetcode problem 153: find minimum in rotated sorted array

link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""


class FindMinimumInRotatedSortedArray:
    def find_min(self, nums: list[int]) -> int:
        """Find min value in rotated sorted array.

        Uses binary search to be super fast.

        Steps:
            - calculate left and right values
            - loop while left is < right
            - if nums[m] > nums[r]
                - then the value has to be in the right side of the list
            - if nums[m] < nums[r]
                then then the value has to be on the left side of the list
            - return nums[l]

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
