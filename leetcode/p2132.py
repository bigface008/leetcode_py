from typing import List


# https://leetcode.com/problems/stamping-the-grid/
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        M, N = len(grid), len(grid[0])
        pre_sum = [[0] * (N + 1) for _ in range(M + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                pre_sum[i + 1][j + 1] = pre_sum[i][j + 1] + pre_sum[i + 1][j] - pre_sum[i][j] + grid[i][j]

        diff = [[0] * (N + 2) for _ in range(M + 2)]
        for i2 in range(stampHeight, M + 1):
            for j2 in range(stampWidth, N + 1):
                i1 = i2 - stampHeight + 1
                j1 = j2 - stampWidth + 1
                if pre_sum[i2][j2] - pre_sum[i1 - 1][j2] - pre_sum[i2][j1 - 1] + pre_sum[i1 - 1][j1 - 1] == 0:
                    diff[i1][j1] += 1
                    diff[i2 + 1][j1] -= 1
                    diff[i1][j2 + 1] -= 1
                    diff[i2 + 1][j2 + 1] += 1

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                diff[i + 1][j + 1] += diff[i][j + 1] + diff[i + 1][j] - diff[i][j]
                if v == 0 and diff[i + 1][j + 1] == 0:
                    return False
        return True