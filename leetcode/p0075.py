# https://leetcode.com/problems/sort-colors/
from typing import List

import utils


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        p0 = p1 = 0
        for i in range(N):
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
            elif nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1


        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # N = len(nums)
        # p0 = p1 = 0
        # for i in range(N):
        #     if nums[i] == 1:
        #         nums[i], nums[p1] = nums[p1], nums[i]
        #         p1 += 1
        #     elif nums[i] == 0:
        #         nums[i], nums[p0] = nums[p0], nums[i]
        #         if p0 < p1:
        #             nums[i], nums[p1] = nums[p1], nums[i]
        #         p0 += 1
        #         p1 += 1


def check(nums: List[int], expect: List[int]):
    temp = nums.copy()
    Solution().sortColors(nums)
    utils.tst(f'nums={temp}', nums, expect)


if __name__ == '__main__':
    check([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
    # check([1, 0, 2], [0, 1, 2])
