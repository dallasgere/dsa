"""leetcode problem 916

link: https://leetcode.com/problems/word-subsets/
"""

from collections import Counter
from collections import defaultdict


class WordSubsets:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        # create the max value counter from words2
        counts_2 = defaultdict(int)

        # merge every counter from words2 into one which contains all the max values
        for w in words2:
            count_w = Counter(w)
            for c, count in count_w.items():
                counts_2[c] = max(counts_2[c], count)

        # compare words1 with counts_2
        res = []
        for w in words1:
            count_w = Counter(w)
            flag = True
            for c, count in counts_2.items():
                if count_w[c] < count:
                    flag = False
                    break

            if flag:
                res.append(w)

        return res
