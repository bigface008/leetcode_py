# https://leetcode.com/problems/first-completely-painted-row-or-column/description/?envType=daily-question&envId=2025-01-20
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        pos_mp = dict()
        for i in range(M):
            for j in range(N):
                pos_mp[mat[i][j]] = (i, j)
        row_mp = [0] * M
        col_mp = [0] * N
        for i, x in enumerate(arr):
            r, c = pos_mp[x]
            row_mp[r] += 1
            if row_mp[r] == N:
                return i
            col_mp[c] += 1
            if col_mp[c] == M:
                return i
        return -1