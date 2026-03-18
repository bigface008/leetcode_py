# https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/?envType=daily-question&envId=2026-03-18
from typing import List, Dict, Optional, Tuple


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        pre_sum = [[0] * (N + 1) for _ in range(M + 1)]
        ans = 0
        for i in range(M):
            for j in range(N):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + grid[i][j]
                if pre_sum[i + 1][j + 1] <= k:
                    ans += 1
        return ans
