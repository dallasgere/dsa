"""leetcode problem 217: Contains Duplicate

link: https://leetcode.com/problems/contains-duplicate/description/
"""


class ContainsDuplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """this determines if a list has duplicates or not

        Args:
            nums (List[int]): the list of numbers to look through

        Returns:
            bool: true if nums contains duplicate, false otherwise
        """
        seen = set()
        for val in nums:
            if val not in seen:
                seen.add(val)
            else:
                return True

        return False
