# https://leetcode.cn/problems/available-captures-for-rook/?envType=daily-question&envId=2024-12-06
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        SIZE = 8
        rook_pos = (0, 0)
        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] == 'R':
                    rook_pos = (i, j)
                    break
        dpos = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ans = 0
        for dx, dy in dpos:
            x, y = rook_pos[0] + dx, rook_pos[1] + dy
            while 0 <= x < SIZE and 0 <= y < SIZE:
                p = board[x][y]
                if p == 'B':
                    break
                elif p == 'p':
                    ans += 1
                    break
                x += dx
                y += dy
        return ans