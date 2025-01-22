# https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/
from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        N = len(nums)
        pre_xor = [0] * (N + 1)
        for i, x in enumerate(nums):
            pre_xor[i + 1] = pre_xor[i] ^ x