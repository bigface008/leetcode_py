from functools import cache
from typing import List
from math import inf

import utils


# https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/description/
# dp[i][j]: ans nums[0...i] andValues[0..j]
# dp[i][j] = min(dp[i - x][j - 1]) + nums[i] for x in [start, end]
class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        N = len(nums)
        M = len(andValues)

        @cache
        def dfs(i: int, j: int, nd: int) -> int:
            if i == N:
                return 0 if j == M else inf
            if j == M:
                return inf
            nd &= nums[i]
            if nd < andValues[j]:
                return inf
            res = dfs(i + 1, j, nd)
            if nd == andValues[j]:
                res = min(res, dfs(i + 1, j + 1, -1) + nums[i])
            return res

        ans = dfs(0, 0, -1)
        return ans if ans < inf else -1


def tst(nums: List[int], andValues: List[int], expect: int):
    output = Solution().minimumValueSum(nums, andValues)
    utils.tst(f'min value sum nums={nums} andValues={andValues}', output, expect)


if __name__ == '__main__':
    tst([1,4,3,3,2], [0,3,3,2], 12)
    tst([2,3,5,7,7,7,5], [0,7,5], )