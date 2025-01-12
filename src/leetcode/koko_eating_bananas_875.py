"""leetcode problem 875: koko eating bananas

link: https://leetcode.com/problems/koko-eating-bananas/description
"""

import math


class KokoEatingBananas:
    """Implementation for koko eating bananas problem.

    Rules:
        - koko can eat at most one pile per hour
            - because of this, h >= len(piles): this is guaranteed
        - the most bananas per hour eaten can only be max(piles)
        - the minimum number of bananas per hour is 1
    """

    def min_eating_speed_three(self, piles: list[int], h: int) -> int:
        """Optimal faster solution using binary search.

        So you are searching for a number(k) within a min and max value
            - this means you can use binary search to look for it instead of assessing each and every number
        """
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + ((r - l) // 2)

            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)

            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

    def min_eating_speed_two(self, piles: list[int], h: int) -> int:
        """neetcode better solution

        This is a solution from neetcode which is a lot better/faster.
        This still fails the time limit on leetcode though.

        Steps:
            - loop to constantly increase k
            - loop through the piles
                - total time to get through a pile is the number in the pile divided by the speed
                - that is how many hours so you can add that time per hour
                    - you have to round up because if you p < k you still have to wait the whole time
            - check if the total time is <= h, if it is then your good, if not you just try a faster speed
        """
        k = 1
        while True:
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)

            if total_time <= h:
                return k

            k += 1

        return k

    def min_eating_speed_one(self, piles: list[int], h: int) -> int:
        """First solution.

        This is my first solution to this problem, it works but it is super slow and fails on time limit in leetcode.

        Steps:
            - loop from min to max number of bananas
            - see if each works in a inner for loop
                - in the inner loop you will loop from 0 to h - 1(which will still equal h)
            - keep track of current pile you are on
                - if current pile is decremented to zero, then you have to move to next pile
            - record k if it works and break out of all the for loops
            - return k

        Thoughts:
            - this solution will be really slow, will try to optimize later
        """
        most = max(piles)
        k = 0
        size = len(piles)
        for num_ban in range(1, most + 1):
            current_pile = 0
            copy = piles[:]
            for hour in range(h):
                copy[current_pile] = copy[current_pile] - num_ban
                if copy[current_pile] <= 0 and current_pile < size:
                    copy[current_pile] = 0
                    current_pile += 1

            if sum(copy) == 0:
                k = num_ban
                break

        return k
