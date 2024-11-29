from typing import List
from math import inf

import utils


# https://leetcode.com/problems/k-concatenation-maximum-sum/
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = pow(10, 9) + 7

        # def dfs(i: int, nums: List[int]) -> int:
        #     if i == 0:
        #         return arr[0]
        #     return max(dfs(i - 1), 0) + nums[i]

        def sol(nums: List[int]):
            dp = 0
            mx = 0
            for x in nums:
                dp = max(dp, 0) + x
                mx = max(dp, mx)
            return mx

        if k == 1:
            return sol(arr) % MOD

        arr2 = arr * 2
        mx2 = sol(arr2)
        ss = sum(arr)
        if ss < 0:
            return max(mx2, 0) % MOD

        return max(0, mx2 - ss + (k - 1) * ss) % MOD


def tst(arr: List[int], k: int, expect: int):
    output = Solution().kConcatenationMaxSum(arr, k)
    utils.tst(f'kConcatenationMaxSum {arr} {k}', output, expect)


if __name__ == '__main__':
    tst([1, -2, 1], 5, 2)
