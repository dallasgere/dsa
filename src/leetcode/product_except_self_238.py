"""leetcode problem 238

link: https://leetcode.com/problems/product-of-array-except-self/description/
"""


class ProductExceptSelf:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """this creates a new array where each element is the product of every other element except its self

        Args:
            nums (list[int]): the original array

        Returns:
            list[int]: the new array where each element is product of every other element except its self
        """
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
