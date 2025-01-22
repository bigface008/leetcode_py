# https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/?envType=daily-question&envId=2025-01-21
from itertools import accumulate
from typing import List
from functools import cache


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        pre_sum = [list(accumulate(p, initial=0)) for p in piles]
        dp = [0] * (k + 1)
        len_sum = 0
        for i in range(1, N + 1):
            len_sum += len(piles[i - 1])
            for j in range(min(k, len_sum), 0, -1):
                dp[j] = max(dp[j - w] + pre_sum[i - 1][w] for w in range(min(j, len(piles[i - 1])) + 1))
        return dp[-1]


class Solution3:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        pre_sum = [list(accumulate(p, initial=0)) for p in piles]
        dp = [[0] * (k + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, k + 1):
                res = 0
                for w in range(min(j, len(piles[i - 1])) + 1):
                    res = max(res, dp[i - 1][j - w] + pre_sum[i - 1][w])
                dp[i][j] = res
        return dp[-1][-1]



class Solution2:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        pre_sum = [list(accumulate(p, initial=0)) for p in piles]

        @cache
        def dfs(i: int, j: int) -> int:
            if i == -1 or j == 0:
                return 0
            ans = 0
            for w in range(min(j, len(piles[i])) + 1):
                ans = max(ans, dfs(i - 1, j - w) + pre_sum[i][w])
            return ans

        return dfs(N - 1, k)
