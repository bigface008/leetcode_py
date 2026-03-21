# https://leetcode.com/problems/flip-square-submatrix-vertically/?envType=daily-question&envId=2026-03-21
from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        for i in range(k // 2):
            r1 = x + i
            r2 = x + k - 1 - i
            arr1 = grid[r1][y:y + k].copy()
            grid[r1][y:y + k] = grid[r2][y:y + k].copy()
            grid[r2][y:y + k] = arr1
        return grid
