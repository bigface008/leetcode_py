# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2025-02-02
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        reverse_cnt = 0
        all_same = True
        for i in range(1, N):
            if all_same and nums[i - 1] != nums[i]:
                all_same = False
            if nums[i - 1] <= nums[i]:
                continue
            reverse_cnt += 1
        if all_same:
            return True
        if nums[0] >= nums[-1]:
            return reverse_cnt == 1
        else:
            return reverse_cnt == 0
