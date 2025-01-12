"""leetcode problem 74: Search a 2D Matrix

link: https://leetcode.com/problems/search-a-2d-matrix/description
"""


class SearchA2DMatrix:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        I think what we can do here is a binary seach through each row.
        This will be a nested loop but it will by O(log(m * n)) because it is:
            - binary search
            - you have to nested loop to iterate through a matrix

        1. I think we can iterate through the matrix and get each row
        2. Pass the row into the binary seach function to search for the method

        binary search function:
            - i think this can just return True if the target is found
            - otherwise I just return false
            - this particular problem does not require the index of the item
        """

        for arr in matrix:
            result = self.binary_search(arr, target)
            if result:
                return True

        return False

    def binary_search(self, arr: list[int], target: int) -> bool:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if arr[l] < target:
                l += 1
            elif arr[r] > target:
                r -= 1
            else:
                return True

        return False
