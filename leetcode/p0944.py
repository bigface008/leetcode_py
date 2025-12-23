# https://leetcode.cn/problems/delete-columns-to-make-sorted/?envType=daily-question&envId=2025-12-20
from typing import List, Dict, Tuple, Optional


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)
        M = len(strs[0])
        ans = 0
        for col in range(M):
            prev: Optional[str] = None
            for i in range(N):
                if prev is not None and prev > strs[i][col]:
                    ans += 1
                    break
                prev = strs[i][col]
        return ans
