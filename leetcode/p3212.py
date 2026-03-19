# https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y/?envType=daily-question&envId=2026-03-19
from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        pre_sum_x = [[0] * (N + 1) for _ in range(M + 1)]
        pre_sum_y = [[0] * (N + 1) for _ in range(M + 1)]
        ans = 0
        for i in range(M):
            for j in range(N):
                pre_sum_x[i + 1][j + 1] = pre_sum_x[i + 1][j] + pre_sum_x[i][j + 1] - pre_sum_x[i][j] + (1 if grid[i][j] == 'X' else 0)
                pre_sum_y[i + 1][j + 1] = pre_sum_y[i + 1][j] + pre_sum_y[i][j + 1] - pre_sum_y[i][j] + (1 if grid[i][j] == 'Y' else 0)
                if pre_sum_x[i + 1][j + 1] == pre_sum_y[i + 1][j + 1] and pre_sum_x[i + 1][j + 1] > 0:
                    ans += 1
        return ans
