from typing import List

import utils


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # N = len(nums)
        # l, r = 0, N - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid
        pass


# Find the smallest i, nums[i] <= target
def bothClose(nums: List[int], target: int) -> int:
    pass


def tst(nums: List[int], target: int, expect: int):
    output = bothClose(nums, target)
    utils.tst(f'test nums={nums} target={target}', output, expect)


if __name__ == '__main__':
    tst()
