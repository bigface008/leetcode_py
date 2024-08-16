from math import inf
from typing import List

import utils


# https://leetcode.cn/problems/maximum-difference-score-in-a-grid/description/?envType=daily-question&envId=2024-08-15
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dp = [[inf for _ in range(N + 1)] for _ in range(M + 1)]
        ans = -inf
        for i in range(M):
            for j in range(N):
                x = grid[i][j]
                minVal = min(dp[i + 1][j], dp[i][j + 1])
                ans = max(ans, x - minVal)
                dp[i + 1][j + 1] = min(minVal, x)
        return ans


def tst(grid: List[List[int]], expect: int):
    output = Solution().maxScore(grid)
    utils.tst(f'max score grid={grid}', output, expect)


if __name__ == '__main__':
    tst([[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]], 9)
    tst([[4, 3, 2], [3, 2, 1]], -1)
