from typing import List
from functools import cache
from math import inf


# dfs(i, j) =

# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        N = len(values)
        f = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N - 2, -1, -1):
            for j in range(i + 2, N):
                res = inf
                for k in range(i + 1, j):
                    res = min(res, f[i][k] + f[k][j] + values[i] * values[j] * values[k])
                f[i][j] = res
        return f[0][len(values) - 1]
        # @cache
        # def dfs(i, j):
        #     if i + 1 == j:
        #         return 0
        #     res = inf
        #     for k in range(i + 1, j):
        #         res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[j] *values[k])
        #     return res
        #
        # return dfs(0, len(values) - 1)