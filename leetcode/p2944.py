# https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/?envType=daily-question&envId=2025-01-24
from typing import List
from math import inf
from functools import cache

# 1 [2, 2]
# 2 [3, 4]
# 3 [4, 6]

# prices[i - 1] + dfs(i - 1)
# j + j >= i
# prices[j - 1] + dfs(j - 1)

#j * 2 >= i
# j >= i / 2


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N = len(prices)
        if N <= 2:
            return prices[0]

        dp = [0] * (N + 1)
        dp[1] = prices[0]
        dp[2] = prices[0]
        for i in range(3, N + 1):
            # res = inf
            # for j in range(i, 0, -1):
            #     if j * 2 < i:
            #         break
            #     res = min(res, dp[j - 1] + prices[j - 1])
            # dp[i] = res
            dp[i] = min(dp[j - 1] + prices[j - 1] for j in range(i, (i + 1) // 2 - 1, -1))
        return dp[-1]

        # N = len(prices)
        # if N <= 2:
        #     return prices[0]
        #
        # dp = [0] * (N + 1)
        # dp[1] = prices[0]
        # dp[2] = prices[0]
        # for i in range(3, N + 1):
        #     res = inf
        #     for j in range(i, 0, -1):
        #         if j * 2 < i:
        #             break
        #         res = min(res, dp[j - 1] + prices[j - 1])
        #     dp[i] = res
        # return dp[-1]


class Solution2:
    def minimumCoins(self, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def dfs(i: int) -> int:
            if i == 1:
                return prices[0]
            if i == 2:
                return prices[0]
            ans = inf
            for j in range(i, 0, -1):
                if j + j < i:
                    break
                ans = min(ans, dfs(j - 1) + prices[j - 1])
            return ans

        return dfs(N)