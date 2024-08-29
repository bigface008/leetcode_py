from typing import List


# https://leetcode.cn/problems/check-if-grid-satisfies-conditions/description/?envType=daily-question&envId=2024-08-29
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if i + 1 < M and grid[i][j] != grid[i + 1][j]:
                    return False
                if j + 1 < N and grid[i][j] == grid[i][j + 1]:
                    return False
        return True