"""leetcode problem 981: Time Based Key Value Store

link: https://leetcode.com/problems/time-based-key-value-store/description
"""


class TimeBasedKeyValueStoreBruteForce:
    """Time based key value store brute force approach.

    Time based key value store brute force approach.
        - The set method is fine
        - Things get goofy in the get method
        - The get method loops through multiplt times at O(n)
        - I also sort the list in there so it just gets too slow

    Things to improve
        - Well since this question is a binary search question I think I should
          be using binary search to look through the list for the right value
    """

    def __init__(self):
        self.store: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_tuple = (value, timestamp)
        if key in self.store:
            self.store[key].append(new_tuple)
        else:
            self.store[key] = []
            self.store[key].append(new_tuple)

        print(self.store)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            count = 0
            for item in self.store[key]:
                if item[1] == timestamp:
                    return item[0]
                count += 1

            if count == len(self.store[key]):
                count = 0
                new_list = [tup for tup in self.store[key]]
                new_list.sort(key=lambda x: x[1])
                for i in range(len(new_list) - 1, -1, -1):
                    if new_list[i][1] <= timestamp:
                        return new_list[i][0]
                    count += 1

                if count == len(new_list):
                    return ""
        else:
            return ""
