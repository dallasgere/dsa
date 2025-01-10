"""leetcode problem 150

link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""


class EvaluateReversePolishNotation:
    def evalRPN(self, tokens: list[str]) -> int:
        """evaluate reverse polish notation

        Args:
            tokens (list[str]): takes list of characters to evaluate

        Returns:
            int: the final computed value
        """

        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]
