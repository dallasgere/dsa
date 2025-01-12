"""leetcode problem 347: Top K Frequent Elements

link: https://leetcode.com/problems/top-k-frequent-elements/description/
"""

from collections import Counter


class TopKFrequentElements:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """this gets top k frequent elements

        Args:
            nums (List[int]): sorting through top k frequent elements
            k (int): the number of elements to find

        Returns:
            List[int]: list of top k most frequent elements
        """
        counted = Counter(nums)
        sorted_count = counted.most_common(k)
        return [item for item, two in sorted_count]

    def topKFrequentConcise(self, nums: list[int], k: int) -> list[int]:
        """just a more concise way to solve this problem

        Args:
            nums (List[int]): sorting through top k frequent elements
            k (int): the number of elements to find

        Returns:
            List[int]: list of top k most frequent elements
        """
        return [item for item, count in Counter(nums).most_common(k)]
