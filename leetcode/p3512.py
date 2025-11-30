# https://leetcode.cn/problems/minimum-operations-to-make-array-sum-divisible-by-k
from typing import List, Dict, Optional, Tuple


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
