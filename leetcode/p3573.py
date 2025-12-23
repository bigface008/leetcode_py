# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/?envType=daily-question&envId=2025-12-17
from typing import List, Dict, Tuple, Optional
from functools import cache
from math import inf


# dfs(day, op_cnt)
# = max(prices[day] - prices[day_i], prices[day_i] - prices[day]) + dfs(day_i, op_cnt - 1) for day_i in [0, day - 2]

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        @cache
        def dfs(day: int, op_cnt: int, state: int) -> int:
            if op_cnt < 0:
                return -inf
            if day < 0:
                return -inf if state != 0 else 0
            p = prices[day]
            if state == 0:
                return max(dfs(day - 1, op_cnt, 0), dfs(day - 1, op_cnt - 1, 1) + p, dfs(day - 1, op_cnt - 1, 2) - p)
            elif state == 1:
                return max(dfs(day - 1, op_cnt, 1), dfs(day - 1, op_cnt - 1, 0) - p)
            else:
                return max(dfs(day - 1, op_cnt, 2), dfs(day - 1, op_cnt - 1, 0) + p)
        ans = dfs(len(prices) - 1, k, 0)
        dfs.cache_clear()
        return ans


        # N = len(prices)
        # dp: List[List[List[int]]] = [[[-inf, -inf, -inf] for _ in range(k + 1)] for _ in range(N)]
        # for op_cnt in range(0, k + 1):
        #     dp[0][op_cnt][0] = 0
        # for day in range(1, N):
        #     for op_cnt in range(1, k + 1):
        #         p = prices[day]
        #         dp[day][op_cnt][0] = max(dp[day - 1][op_cnt][0], dp[day - 1][op_cnt - 1][1] + p, dp[day - 1][op_cnt - 1][2] - p)
        #         dp[day][op_cnt][1] = max(dp[day - 1][op_cnt - 1][0] - p, dp[day - 1][op_cnt][1])
        #         dp[day][op_cnt][2] = max(dp[day - 1][op_cnt - 1][0] + p, dp[day - 1][op_cnt][2])
        # return dp[-1][-1][0]

# class Solution:
#     def maximumProfit(self, prices: List[int], k: int) -> int:
#         N = len(prices)
#         dp = [[0] * (k + 1) for _ in range(N)]
#         for day in range(1, N):
#             for op_cnt in range(1, k + 1):
#                 max_price, min_price = prices[day], prices[day]
#                 if day == 1:
#                     dp[day][op_cnt] = max(prices[0], prices[1]) - min(prices[0], prices[1])
#                     continue
#                 res = 0
#                 for day_i in range(day - 1, -1, -1):
#                     min_price = min(prices[day_i], min_price)
#                     max_price = max(prices[day_i], max_price)
#                     res = max(res, max_price - min_price + ((dp[day_i - 1][op_cnt - 1]) if day_i != 0 else 0))
#                 dp[day][op_cnt] = res
#         return dp[N - 1][k]

# class Solution:
#     def maximumProfit(self, prices: List[int], k: int) -> int:
#         N = len(prices)
#
#         @cache
#         def dfs(day: int, op_cnt: int) -> int:
#             if day <= 0 or op_cnt <= 0:
#                 return 0
#             max_price, min_price = prices[day], prices[day]
#
#             res = 0
#             for day_i in range(day - 1, -1, -1):
#                 min_price = min(prices[day_i], min_price)
#                 max_price = max(prices[day_i], max_price)
#                 res = max(res, max_price - min_price + dfs(day_i - 1, op_cnt - 1))
#             return res
#
#         return dfs(N - 1, k)


if __name__ == '__main__':
    print(Solution().maximumProfit([1, 7, 9, 8, 2], 2))
