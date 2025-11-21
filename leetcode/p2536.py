# https://leetcode.com/problems/increment-submatrices-by-one/description/?envType=daily-question&envId=2025-11-14
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = diff[i][j]
                if i > 0:
                    res[i][j] += res[i - 1][j]
                if j > 0:
                    res[i][j] += res[i][j - 1]
                if i > 0 and j > 0:
                    res[i][j] -= res[i - 1][j - 1]
        return res