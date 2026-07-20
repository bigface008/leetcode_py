# https://leetcode.cn/problems/shift-2d-grid/?envType=daily-question&envId=2026-07-20
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        k = k % (M * N)
        row_change = k // N
        col_change = k % N
        res = [[0] * N for _ in range(M)]
        for r in range(M):
            source_row = grid[r]
            target_row_idx = (r + row_change) % M
            for c in range(N):
                target_c = c + col_change
                if target_c >= N:
                    target_c %= N
                    res[(target_row_idx + 1) % M][target_c] = grid[r][c]
                else:
                    res[target_row_idx][target_c] = grid[r][c]
        return res