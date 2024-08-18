from typing import List
from functools import cache
from math import inf


# dfs(i, b)
# if b:
#   dfs(i, true) = max(dfs(i - 1, false) - prices[i], dfs(i - 1, true))
# else:
#   dfs(i, false) = max(dfs(i - 1, true) + prices[i], dfs(i - 1, false))
# max(dfs(...))


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = -inf
        N = len(prices)
        f0 = 0
        f1 = -inf
        for i in range(N):
            new_f0 = max(f1 + prices[i], f0)
            f1 = max(f0 - prices[i], f1)
            f0 = new_f0
        return f0
        # f = [[0, 0] for _ in range(N + 1)]
        # f[0][0] = 0
        # f[0][1] = -inf
        # for i in range(N):
        #     f[i + 1][1] = max(f[i][0] - prices[i], f[i][1])
        #     f[i + 1][0] = max(f[i][1] + prices[i], f[i][0])
        # return f[N][0]
        # @cache
        # def dfs(i: int, b: bool) -> int:
        #     if i < 0:
        #         return 0 if not b else -prices[0]
        #     if b:
        #         return max(dfs(i - 1, False) - prices[i], dfs(i - 1, True))
        #     else:
        #         return max(dfs(i - 1, True) + prices[i], dfs(i - 1, False))
        #
        # return dfs(N - 1, False)
