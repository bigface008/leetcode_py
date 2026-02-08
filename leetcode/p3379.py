# https://leetcode.com/problems/transformed-array/?envType=daily-question&envId=2026-02-05
from typing import List, Dict, Tuple


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [0] * N
        for i, x in enumerate(nums):
            result[i] = nums[(i + x + N) % N]
        return result
