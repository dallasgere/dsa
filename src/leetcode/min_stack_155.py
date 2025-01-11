"""leetcode problem 155

link: https://leetcode.com/problems/min-stack/description/
"""

class MinStack:
    """
    We need two stacks.
    1. one to keep track of the actual values
    2. the second keeps track of the min value per each element in the stack
    """
    def __init__(self):
        self.vals = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.vals:
            self.vals.append(val)
            self.mins.append(val)
        elif self.vals:
            self.vals.append(val)
            if val < self.mins[-1]:
                self.mins.append(val)
            else:
                smallest = self.mins[-1]
                self.mins.append(smallest)

    def pop(self) -> None:
        """
        this needs to be pop method because the remove method is O(n)
        pop method is O(1)
        """
        self.vals.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.mins[-1]
