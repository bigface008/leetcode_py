# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/?envType=daily-question&envId=2025-12-10
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        N = len(complexity)
        MOD = pow(10, 9) + 7
        for i, c in enumerate(complexity):
            if i != 0 and c <= complexity[0]:
                return 0
        ans = 1
        for i in range(1, N):
            ans *= i
            ans %= MOD
        return ans