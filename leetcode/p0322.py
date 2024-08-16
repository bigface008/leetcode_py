from typing import List
from functools import cache
from math import inf


# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [inf] * (amount + 1)
        f[0] = 0
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount]
        return ans if ans < inf else -1



# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         f = [[inf] * (amount + 1) for _ in range(n + 1)]
#         f[0][0] = 0
#         for i in range(1, n + 1):
#             for j in range(amount + 1):
#                 if j < coins[i - 1]:
#                     f[i][j] = f[i - 1][j]
#                 else:
#                     f[i][j] = min(f[i - 1][j], f[i][j - coins[i - 1]] + 1)
#         ans = f[n][amount]
#         return ans if ans < inf else -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @cache
#         def dfs(i: int, a: int):
#             if i < 0:
#                 return 0 if a == 0 else inf
#             if a < coins[i]:
#                 return dfs(i - 1, a)
#             return min(dfs(i - 1, a), dfs(i, a - coins[i]) + 1)
#
#         ans = dfs(len(coins) - 1, amount)
#         return ans if ans < inf else -1
