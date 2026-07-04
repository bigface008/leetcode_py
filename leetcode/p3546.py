# https://leetcode.com/problems/equal-sum-grid-partition-i/?envType=daily-question&envId=2026-03-25
from typing import List, Dict, Tuple


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        pre_row_sum = [0] * (M + 1)
        pre_col_sum = [0] * (N + 1)
        for i, row in enumerate(grid):
            pre_row_sum[i + 1] = pre_row_sum[i] + sum(row)
        for j in range(N):
            pre_col_sum[j + 1] = pre_col_sum[j] + sum(grid[i][j] for i in range(M))
        for i in range(M - 1):
            top_sum = pre_row_sum[i + 1]
            bottom_sum = pre_row_sum[-1] - top_sum
            if top_sum == bottom_sum:
                return True
        for j in range(N - 1):
            left_sum = pre_col_sum[j + 1]
            right_sum = pre_col_sum[-1] - left_sum
            if left_sum == right_sum:
                return True
        return False
