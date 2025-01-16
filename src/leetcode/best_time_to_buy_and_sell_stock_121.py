"""leetcode problem 121: Best Time to Buy and Sell Stock

link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class BestTimeToBuyAndSellStock:
    def solution(self, prices: list[int]) -> int:
        """Find max profit from a list of stock prices.

        Sliding window algorithm which keeps track of the smallest value and updates it accordingly
        """
        res = 0
        sm = max(prices)
        for i, val in enumerate(prices):
            if val < sm:
                sm = val
            else:
                res = max(res, val - sm)

        return res
