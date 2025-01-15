"""leetcode problem 2657:

link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description
"""


class FindThePrefixCommonArrayOfTwoArrays:
    def solution(self, A: list[int], B: list[int]) -> list[int]:
        """find the prefix common array of two arrays

        Args:
            A (list[int]): the first permutation array
            B (list[int]): the second permutation array

        Returns:
            list[int]: list where list[i] is the number of common values between A and B up to that indice
        """

        res = []
        a_set = set()
        b_set = set()
        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])
            total = self.count_common(a_set, b_set)
            res.append(total)

        return res

    def count_common(self, a_set: set, b_set: set) -> int:
        total_common = 0
        for i in a_set:
            if i in b_set:
                total_common += 1

        return total_common
