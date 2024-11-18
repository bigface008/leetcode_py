from typing import List
from functools import cache
import bisect

import utils


# Given an array A[1 . . . n] of n distinct numbers between 1 to n, compute
# the number of inversions for every A[1 . . . i]. Two array elements A[i] and A[j] form
# an inversion if A[i] > A[j] and i < j. You should output n different answers, one for
# each A[1 . . . i]. The expected time complexity is O(n log n).

def solution(nums: List[int]) -> List[int]:
    N = len(nums)
    ans = [0] * N
    indices = list(range(N))
    temp = indices.copy()

    def dfs(left: int, right: int):
        if left == right:
            return
        if left + 1 == right:
            if nums[indices[left]] > nums[indices[right]]:
                ans[indices[right]] += 1
                indices[left], indices[right] = indices[right], indices[left]
            return
        mid = (left + right) // 2
        dfs(left, mid)
        dfs(mid + 1, right)

        for k in range(left, right + 1):
            temp[k] = indices[k]

        k = left
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[temp[i]] < nums[temp[j]]:
                indices[k] = temp[i]
                i += 1
            else:
                indices[k] = temp[j]
                ans[indices[k]] += mid - i + 1
                j += 1
            k += 1
        while i <= mid:
            indices[k] = temp[i]
            i += 1
            k += 1
        while j <= right:
            indices[k] = temp[j]
            j += 1
            k += 1

    dfs(0, N - 1)
    for i in range(1, N):
        ans[i] += ans[i - 1]
    return ans


# def solution(nums: List[int]) -> List[int]:
#     N = len(nums)
#     ans = [0] * N
#
#     for i in range(1, N):
#         x = nums[i]
#         idx = bisect.bisect_left(nums, x, 0, i)
#         for j in range(i, idx, -1):
#             nums[j] = nums[j - 1]
#         nums[idx] = x
#         ans[i] = i - idx + ans[i - 1]
#     return ans

    # indices = list(range(N))
    # temp = indices.copy()
    #
    # def dfs(left: int, right: int):
    #     if left == right:
    #         return
    #     if left + 1 == right:
    #         if nums[indices[left]] > nums[indices[right]]:
    #             ans[indices[left]] += 1
    #         return
    #
    #     mid = (left + right) // 2
    #     dfs(left, mid)
    #     dfs(mid + 1, right)
    #
    #     # merge
    #
    #     ans[]


def tst(nums: List[int], expect: List[int]):
    output = solution(nums)
    utils.tst(f'sol nums={nums}', output, expect)


if __name__ == '__main__':
    tst([5, 2, 6, 1], [0, 1, 1, 4])
    tst([13, 21, 9, 8, 7, 6], [0, 0, 2, 5, 9, 14])
    tst([5, 4, 3, 2, 1], [0, 1, 3, 6, 10])
    tst([1, 2, 3, 4, 5], [0, 0, 0, 0, 0])
