"""monotomic stack implementation

Simple class to show a few implementations of monotomic stack.
"""


class MonotomicStack:
    """Class that contanis a few functions for monotomic stack.

    MonotomicStack:
        - next greatest element
        - next smaller element
        - previous greater element
        - previous smaller element
    """

    def next_greater_element_values(self, arr: list) -> list:
        """monotomic stack for finding next greatest values

        Args:
            arr (list): the array to process

        Returns:
            list: list of values where the value is the next greatest value from that current index
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = arr[i]

            stack.append(i)

        return result

    def next_greater_element_indices(self, arr: list) -> list:
        """monotomic stack for finding next greatest indices

        Args:
            arr (list): the array to process

        Returns:
            list: list of indices showing where the next greatest value is located in the array
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i

            stack.append(i)

        return result

    def next_smaller_element_values(self, arr: list) -> list:
        """monotomic stack to find next smallest elements

        Args:
            arr (list): array to process

        Returns:
            list: list where each value is the value of the next smallest element from that index
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = arr[i]

            stack.append(i)

        return result

    def next_smaller_element_indices(self, arr: list) -> list:
        """monotomic stack to find next smallest elements indices

        Args:
            arr (list): array to process

        Returns:
            list: list of indices to show where the next smallest element is
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i

            stack.append(i)

        return result

    def previous_greater_element_values(self, arr: list) -> list:
        """monotomic stack to find previous greatest values

        Args:
            arr (list): array to process

        Returns:
            list: list of previous greatest values
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] > arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = arr[i]

            stack.append(i)

        return result

    def previous_greater_element_indices(self, arr: list) -> list:
        """monotomic stack to get list of previous greater indices

        Args:
            arr (list): array to process

        Returns:
            list: list of indices of the previous greater element
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] > arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i

            stack.append(i)

        return result

    def previous_smaller_element_values(self, arr: list) -> list:
        """monotomic stack to get previous smaller values

        Args:
            arr (list): array to process

        Returns:
            list: list of previous smaller values
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = arr[i]

            stack.append(i)

        return result

    def previous_smaller_element_indices(self, arr: list) -> list:
        """monotomic stack to get previous smaller values indices

        Args:
            arr (list): array to process

        Returns:
            list: list previous smaller values indices
        """
        stack = []
        result = [-1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i

            stack.append(i)

        return result
