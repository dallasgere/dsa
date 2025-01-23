"""leetcode problem 567: Permutation in String

link: https://leetcode.com/problems/permutation-in-string/description/
"""


class PermutationInString:
    def solution_one(self, s1: str, s2: str) -> bool:
        """checks if permutation of s1 exists in s2

        - This is the first solution I came up with.
        - This is definitely not the most optimal, but it is far from the least optimal

        Args:
            s1 (str): string to check if its in s2
            s2 (str): string to check if it contains s1

        Returns:
            bool: true if permutation of s1 exists in s2
        """

        l, r = 0, len(s1)
        for i in range(len(s2)):
            window = s2[l:r]
            if len(window) == len(s1):
                if "".join(sorted(window)) == "".join(sorted(s1)):
                    return True

            l += 1
            r += 1

        return False
