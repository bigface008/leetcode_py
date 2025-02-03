# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2025-02-03
from typing import List

import utils


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 1
        inc_cnt = 1
        dec_cnt = 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                dec_cnt = 1
                inc_cnt += 1
                ans = max(ans, inc_cnt)
            elif nums[i] < nums[i - 1]:
                inc_cnt = 1
                dec_cnt += 1
                ans = max(ans, dec_cnt)
            else:
                dec_cnt = 1
                inc_cnt = 1
        return ans


def check(nums: List[int], expect: int) -> int:
    output = Solution().longestMonotonicSubarray(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    check([1, 4, 3, 3, 2], 2)
