# https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/description/?envType=daily-question&envId=2026-03-02
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        trail_zeros = [N] * N
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if grid[i][j]:
                    trail_zeros[i] = N - j - 1
                    break

        ans = 0
        for i in range(N):
            need_zeros = N - i - 1
            found = False
            for j in range(i, N):
                if trail_zeros[j] >= need_zeros:
                    ans += j - i
                    trail_zeros[i + 1:j + 1] = trail_zeros[i:j]
                    found = True
                    break
            if not found:
                return -1
        return ans
