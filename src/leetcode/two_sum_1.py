class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in prev:
                return [prev[diff], i]

            prev[val] = i

        return []
