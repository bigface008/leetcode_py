# https://leetcode.com/problems/count-servers-that-communicate/?envType=daily-question&envId=2025-01-23
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        row_cnt = [0] * M
        col_cnt = [0] * N
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    ans += 1
        return ans