# https://leetcode.cn/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2025-12-25
from typing import List, Dict, Optional, Tuple
import heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for seq in range(k):
            val = happiness[seq]
            if val <= seq:
                break
            ans += val - seq
        return ans