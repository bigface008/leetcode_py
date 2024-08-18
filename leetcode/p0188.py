from typing import List
from math import inf
from functools import cache

import utils


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        f = [[-inf, -inf] for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0
        for i, price in enumerate(prices):
            for j in range(1, k + 2):
                f[j][0] = max(f[j][0], f[j - 1][1] + price)
                f[j][1] = max(f[j][1], f[j][0] - price)
        return f[k + 1][0]
        # f = [[[-inf, -inf] for _ in range(k + 2)] for _ in range(N + 1)]
        # for j in range(1, k + 2):
        #     f[0][j][0] = 0
        # for i, price in enumerate(prices):
        #     for j in range(1, k + 2):
        #         f[i + 1][j][0] = max(f[i][j][0], f[i][j - 1][1] + price)
        #         f[i + 1][j][1] = max(f[i][j][1], f[i][j][0] - price)
        # return f[N][k + 1][0]
        # @cache
        # def dfs(i: int, j: int, hold: bool) -> int:
        #     if i < 0:
        #         return -inf if hold else 0
        #     if j < 0:
        #         return 0
        #     if hold:
        #         return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
        #     else:
        #         return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])
        #
        # return dfs(N - 1, k, False)


def tst(k: int, prices: List[int], expect: int):
    output = Solution().maxProfit(k, prices)
    utils.tst(f'max profit k={k} prices={prices}', output, expect)


if __name__ == '__main__':
    tst(2, [2, 4, 1], 2)
    tst(2, [3, 2, 6, 5, 0, 3], 7)
