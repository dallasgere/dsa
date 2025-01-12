"""leetcode problem 875: koko eating bananas

link: https://leetcode.com/problems/koko-eating-bananas/description
"""


class KokoEatingBananas:
    """Implementation for koko eating bananas problem.

    Rules:
        - koko can eat at most one pile per hour
            - because of this, h >= len(piles): this is guaranteed
        - the most bananas per hour eaten can only be max(piles)
        - the minimum number of bananas per hour is 1
    """

    def min_eating_speed_one(self, piles: list[int], h: int) -> int:
        """First solution.

        This is my first solution to this problem, it works but it is super slow and fails on time limit in leetcode.
            - I think it is really ugly and convoluted at the moment
            - it is slow which I will try to fix ugly first then optimize for speed

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
            - This algorithm is like super ugly so I will try and fix that
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
