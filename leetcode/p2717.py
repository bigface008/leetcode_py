# https://leetcode.cn/problems/semi-ordered-permutation/?envType=daily-question&envId=2024-12-11
from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        N = len(nums)
        if nums[0] == 1 and nums[-1] == N:
            return 0
        ans = 0
        one_pos = -1
        max_pos = -1
        for i, x in enumerate(nums):
            if x == 1:
                one_pos = i
                if max_pos != -1:
                    break
            elif x == N:
                max_pos = i
                if one_pos != -1:
                    break
        if one_pos < max_pos:
            return one_pos + N - 1 - max_pos
        else:
            return one_pos + N - 1 - max_pos - 1
