"""leetcode problem 22

link: https://leetcode.com/problems/generate-parentheses/description/
"""


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> list[str]:
        """Function to generate all combinations of n pairs of valid parenthesis.

        Rules:
            1. can only append open parenthesis when open_count < n
            2. can only append closed parenthesis when closed_count < n
            3. done once open_count == closed_count == n

        Constraints:
            1 <= n <= 8

        Args:
            n (int): how many pairs of parenthesis to use

        Returns:
            list[str]: list of all combinations of n paurs of valid parenthesis
        """

        stack = []
        res = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()

            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()

        backtrack(0, 0)
        return res
