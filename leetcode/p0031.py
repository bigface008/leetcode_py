import collections
from typing import List
import bisect

import utils


# https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)
        if N <= 1:
            return
        if N == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        if nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return

        left = N - 2
        while left >= 0:
            expand = True
            pivot = -1
            pivot_idx = -1
            if nums[left] < nums[left + 1]:
                expand = False
                pivot = nums[left]
                pivot_idx = left
            if expand:
                if left == 0:
                    nums.reverse()
                    return
                left -= 1
                continue
            mid = (pivot_idx + 1 + N - 1) // 2
            for i in range(pivot_idx + 1, mid + 1):
                i2 = N - 1 - (i - pivot_idx - 1)
                nums[i], nums[i2] = nums[i2], nums[i]
            bigger_idx = bisect.bisect_left(range(pivot_idx + 1, N), True,
                                            key=lambda idx: nums[idx] > pivot) + pivot_idx + 1
            nums[bigger_idx], nums[pivot_idx] = nums[pivot_idx], nums[bigger_idx]
            break


# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         N = len(nums)
#         if N <= 1:
#             return
#         if N == 2:
#             nums[0], nums[1] = nums[1], nums[0]
#             return
#         if nums[-1] > nums[-2]:
#             nums[-1], nums[-2] = nums[-2], nums[-1]
#             return
#
#         def rec(left: int, right: int):
#             expand = True
#             pivot = -1
#             pivot_idx = -1
#             for i in range(left, right):
#                 if nums[i] < nums[i + 1]:
#                     expand = False
#                     pivot = nums[i]
#                     pivot_idx = i
#                     break
#             if expand:
#                 if left == 0:
#                     nums.reverse()
#                     return
#                 rec(left - 1, right)
#                 return
#             mid = (pivot_idx + 1 + right) // 2
#             for i in range(pivot_idx + 1, mid + 1):
#                 i2 = right - (i - pivot_idx - 1)
#                 nums[i], nums[i2] = nums[i2], nums[i]
#             bigger_idx = bisect.bisect_left(range(pivot_idx + 1, right + 1), True,
#                                             key=lambda idx: nums[idx] > pivot) + pivot_idx + 1
#             nums[bigger_idx], nums[pivot_idx] = nums[pivot_idx], nums[bigger_idx]
#
#         rec(N - 2, N - 1)


def tst(nums: List[int], expect: int):
    nn = nums.copy()
    Solution().nextPermutation(nums)
    utils.tst(f'next permutation nums={nn}', nums, expect)


# def doSomething():
#     arr = [2, 3, 4, 5, 6]
#     pivot = 1
#     idx = bisect.bisect_left(range())


if __name__ == '__main__':
    tst([1, 3, 2], [2, 1, 3])
    # tst([5, 1, 1], [1, 1, 5])
