# https://leetcode.cn/problems/knight-probability-in-chessboard/description/?envType=daily-question&envId=2024-12-07
from functools import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dpos = ((-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2))

        @cache
        def dfs(r: int, c: int, step: int) -> float:
            if not (0 <= r < n) or not (0 <= c < n):
                return 0
            if step == k:
                return 1
            res = 0
            for dx, dy in dpos:
                x, y = r + dx, c + dy
                res += dfs(x, y, step + 1)
            res /= 8
            return res

        return dfs(row, column, 0)