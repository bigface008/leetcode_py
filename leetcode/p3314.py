# https://leetcode.cn/problems/construct-the-minimum-bitwise-array-i/?envType=daily-question&envId=2026-01-20
from typing import List


# x
# a or (a + 1) == x
# last k digits of a


# x x x 0 1 1 1
# x x x 1 0 0 0

# x x x 1 1 1 1
# x x 1 0 0 0 0

# x x x 1 0 1 1
# x x x 1 1 0 0


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [-1] * N
        for i, x in enumerate(nums):
            right_1_cnt = 0
            val = x
            while x > 0:
                if x & 1 == 1:
                    right_1_cnt += 1
                else:
                    break
                x >>= 1
            if right_1_cnt == 0:
                continue
            ans[i] = val - (1 << (right_1_cnt - 1))
        return ans