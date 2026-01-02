# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/?envType=daily-question&envId=2026-01-02
from typing import List, Dict, Tuple, Optional, Set
from math import inf


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen: Set[int] = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
        return None