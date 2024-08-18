from typing import List
from functools import cache
from math import inf

# dfs(i, true) = max(dfs(i - 1, true), dfs(i - 1, false) - prices[i])
# dfs(i, false) = max(dfs(i - 1, false), dfs(i - 2, true) + prices[i - 1])

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            else:
                return max(dfs(i - 1, False), dfs(i - 2, True) + prices[i - 1])

        return dfs(len(prices) - 1, False)