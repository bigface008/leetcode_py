# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/?envType=daily-question&envId=2025-11-22
from typing import List, Dict, Tuple, Optional


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            remain = x % 3
            if remain != 0:
                ans += 1
        return ans