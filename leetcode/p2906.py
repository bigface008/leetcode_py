# https://leetcode.cn/problems/construct-product-matrix/?envType=daily-question&envId=2026-03-24
from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N, M = len(grid), len(grid[0])
        MOD = 12345
        ans = [[0] * M for _ in range(N)]

        suf = 1
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                ans[i][j] = suf % MOD
                suf = suf * grid[i][j] % MOD

        pre = 1
        for i in range(N):
            for j in range(M):
                ans[i][j] = ans[i][j] * pre % MOD
                pre = pre * grid[i][j] % MOD

        return ans
