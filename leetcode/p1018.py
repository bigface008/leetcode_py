# https://leetcode.com/problems/binary-prefix-divisible-by-5/?envType=daily-question&envId=2025-11-24
from typing import List, Dict, Optional, Tuple


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        N = len(nums)
        ans = [False] * N
        x = 0
        for i, b in enumerate(nums):
            x = x * 2 + b
            ans[i] = (x % 5) == 0
        return ans