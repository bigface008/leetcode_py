# https://leetcode.cn/problems/delete-columns-to-make-sorted-iii/?envType=daily-question&envId=2025-12-22
from typing import List, Dict, Tuple, Optional


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N, M = len(strs), len(strs[0])
        f = [0] * M
        for col_i in range(M):
            for col_j in range(col_i):
                if f[col_j] > f[col_i] and all(s[col_j] <= s[col_i] for s in strs):
                    f[col_i] = f[col_j]
            f[col_i] += 1
        return M - max(f)