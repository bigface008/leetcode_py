# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2025-01-14
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        sa, sb = 0, 0
        ans = [0] * N
        for i in range(N):
            a = A[i]
            b = B[i]
            sa |= 1 << a
            sb |= 1 << b
            ans[i] = (sa & sb).bit_count()
        return ans