import heapq
from typing import List, Optional
from math import inf

import utils


# https://leetcode.cn/problems/132-pattern/description/
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        stk = []
        k = -inf
        for i in range(N - 1, -1, -1):
            x = nums[i]
            if x < k:
                return True
            while stk and stk[-1] < x:
                k = max(k, stk.pop())
            stk.append(x)
        return False

    # def find132pattern(self, nums: List[int]) -> bool:
    #     N = len(nums)
    #     pre_min: List[Optional[int]] = [None] * N
    #     curr_min = nums[0]
    #     for i in range(1, N):
    #         x = nums[i]
    #         if curr_min < x:
    #             pre_min[i] = curr_min
    #         else:
    #             curr_min = x
    #             pre_min[i] = None
    #
    #     for j in range(1, N):
    #         tmp = pre_min[j]
    #         if tmp is None:
    #             continue
    #         for k in range(j + 1, N):
    #             if tmp < nums[k] < nums[j]:
    #                 return True
    #     return False

        # N = len(nums)
        # for i in range(N - 2):
        #     for j in range(i + 1, N - 1):
        #         if nums[i] >= nums[j]:
        #             continue
        #         for k in range(j + 1, N):
        #             if nums[j] > nums[k] > nums[i]:
        #                 print(nums[i], nums[j], nums[k])
        #                 return True
        # return False


def tst(nums: List[int], expect: bool):
    output = Solution().find132pattern(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    tst([1, 0, 1, -4, -3], False)
