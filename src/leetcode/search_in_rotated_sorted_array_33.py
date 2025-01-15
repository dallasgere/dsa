"""leetcode problem 33: Search in Rotated Sorted Array

link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""


class SearchInRotatedSortedArray:
    def search_in_rotated_sorted_array(self, nums: list[int], target: int) -> int:
        """solution and thoughts.

        Logic:
            - Find the pivot index.
            - Slice the array into the two sides from the pivot index.
            - Perform regular binary search on the two arrays.
            - If the first slice contains the target then you return that index.
            - If the second slice contains the target then you have to add the
              length of the first array to the second one to match the size
              of the original array.
        """
        min_index = self.find_min_index(nums)
        one = nums[:min_index]
        two = nums[min_index:]
        res_one = self.binary_search(one, target)
        res_two = self.binary_search(two, target)

        if res_one == res_two == -1:
            return -1
        elif res_one != -1:
            return res_one
        elif res_two != -1:
            return res_two + len(one)

    def binary_search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1

    def find_min_index(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        return l
