# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/?envType=daily-question&envId=2026-01-10
from itertools import accumulate
from typing import List, Optional, Dict
from math import inf
from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        total_sum = sum(map(ord, s1)) + sum(map(ord, s2))
        N1, N2 = len(s1), len(s2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(N1):
            for j in range(N2):
                x, y = s1[i], s2[j]
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + ord(x) + ord(y)
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return total_sum - dp[-1][-1]

        # pre_sum_1 = list(accumulate((ord(s) for s in s1), initial=0))
        # pre_sum_2 = list(accumulate((ord(s) for s in s2), initial=0))
        #
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i < 0:
        #         return pre_sum_2[j + 1]
        #     if j < 0:
        #         return pre_sum_1[i + 1]
        #     res = inf
        #     r1 = dfs(i - 1, j)
        #     r2 = dfs(i, j - 1)
        #     r3 = dfs(i - 1, j - 1)
        #     if r1 is not inf:
        #         res = min(res, r1 + ord(s1[i]))
        #     if r2 is not inf:
        #         res = min(res, r2 + ord(s2[j]))
        #     if r3 is not inf:
        #         res = min(res, r3 + (0 if s1[i] == s2[j] else (ord(s1[i]) + ord(s2[j]))))
        #     # print(f'dfs({i}, {j}) = {res}')
        #     return res
        #
        # return dfs(len(s1) - 1, len(s2) - 1)


if __name__ == '__main__':
    print(Solution().minimumDeleteSum('sea', 'eat'))
