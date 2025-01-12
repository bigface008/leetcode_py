# https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/?envType=daily-question&envId=2025-01-12
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        M = max(candidates).bit_length()
        bits = [0] * M
        for x in candidates:
            for b in range(M):
                if x & (1 << b) != 0:
                    bits[b] += 1
        return max(bits)