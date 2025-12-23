from typing import List
from functools import cache
import bisect

import utils


# dfs(i)

# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = 1
        ans = 1
        for i in range(1, N):
            prev_len = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    prev_len = max(prev_len, dp[j])
            dp[i] = prev_len + 1
            ans = max(ans, dp[i])
        return ans

        # dp[i] =
        #   if nums[i] > nums[i - 1]:
        #     dp[i - 1] + 1
        #   else:
        #     0

        # N = len(nums)
        # ans = 0
        # f = [0] * N
        # for i in range(N):
        #     temp = 0
        #     for j in range(i, -1, -1):
        #         if nums[j] < nums[i]:
        #             temp = max(temp, f[j])
        #     f[i] = temp + 1
        #     ans = max(f[i], ans)
        #
        # return ans

        # N = len(nums)
        # ans = 0
        # f = [0] * N
        # numToMaxLen = {}
        # ns = []  # distinct & sorted
        # for i in range(N):
        #     idx = -1
        #     pos = bisect.bisect_left(ns, nums[i])
        #     ns.insert(pos, nums[i])
        #     pos -= 1
        #     if pos < 0:  # no smaller num
        #         f[i] = 1
        #         numToMaxLen[nums[i]] = 1
        #     else:
        #         f[i] = numToMaxLen[ns[pos]] + 1
        #         numToMaxLen[nums[i]] = f[i]
        #     ans = max(ans, f[i])
        # return ans


def tst(nums: List[int], expect: int):
    output = Solution().lengthOfLIS(nums)
    utils.tst(f'length of LIS nums={nums}', output, expect)


if __name__ == '__main__':
    tst([10, 9, 2, 5, 3, 7, 101, 18], 4)
    tst([0, 1, 0, 3, 2, 3], 4)
    tst([7, 7, 7, 7, 7, 7, 7], 1)
