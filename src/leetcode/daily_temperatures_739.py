"""leetcode problem 739: Daily Temperatures

link: https://leetcode.com/problems/daily-temperatures/description/
"""


class DailyTemperatures:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        We need to use a monotomic stack for this.
        Building a monotomic stack requires a for loop and a while loop within the for loop
        Monotomic stack:
            - maintain elements in strictly increasing or decreasing order
            - can find next greater element
            - can find next smaller element
            - can find previous greater element
            - can find previous smaller element
        """

        # this is the monotomic stack portion
        n = len(temperatures)
        stack = []
        next_greater = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                next_greater[previous_index] = i

            stack.append(i)

        # this portion figures out how long it will be until the next warmest day
        result = []
        for i, val in enumerate(next_greater):
            if val == 0:
                result.append(0)
            else:
                result.append(val - i)

        return result
