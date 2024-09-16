from itertools import accumulate
from typing import List

import utils


# https://leetcode.cn/problems/points-that-intersect-with-cars/?envType=daily-question&envId=2024-09-15
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        max_end = max(end for _, end in nums)
        diff = [0] * (max_end + 2)
        for start, end in nums:
            diff[start] += 1
            diff[end + 1] -= 1
        return sum(s > 0 for s in accumulate(diff))


        # nums.sort()
        # ans = 0
        # left, right = 0, 0
        # for i, (l, r) in enumerate(nums):
        #     if right >= l:
        #         if right <= r:
        #             right = r
        #     else:
        #         if right != 0:
        #             ans += right - left + 1
        #         left = l
        #         right = r
        # if right != 0:
        #     ans += right - left + 1
        # return ans


def tst(nums: List[List[int]], expect: int):
    output = Solution().numberOfPoints(nums)
    utils.tst(f'numberOfPoints nums={nums}', output, expect)


def diff_learn():
    nums = [1, 13, 22, 5, 21, 43, 0, 2, 6, 9, 90, 6, 23]
    N = len(nums)
    diff = [0] * N
    diff[0] = nums[0]
    for i in range(1, N):
        diff[i] = nums[i] - nums[i - 1]
    after = list(accumulate(diff))
    print(f'diff={diff} after={after} after==nums {after == nums}')

    diff[3] += 10
    diff[7] -= 10
    after = list(accumulate(diff))
    print(f'diff={diff} after={after}')


if __name__ == '__main__':
    # tst([[3, 6], [1, 5], [4, 7]], 7)
    # tst([[1, 3], [5, 8]], 7)
    diff_learn()
