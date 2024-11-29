from itertools import accumulate
from typing import List
from functools import cache


# https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/description/?envType=daily-question&envId=2024-11-29
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)
        M = max(nums) + 1
        MOD = pow(10, 9) + 7

        dp = [[0] * M for _ in range(N)]
        for x in range(nums[0] + 1):
            dp[0][x] = 1
        for i in range(1, N):
            pre_sum = list(accumulate(dp[i - 1]))
            for x in range(nums[i] + 1):
                max_prev = min(nums[i - 1] - nums[i], 0) + x
                dp[i][x] = pre_sum[max_prev] % MOD if max_prev >= 0 else 0

        return sum(dp[-1]) % MOD


        # @cache
        # def dfs(idx: int, val: int) -> int:
        #     v2 = nums[idx] - val
        #     if val < 0 or v2 < 0:
        #         return 0
        #     if idx == 0:
        #         return 1
        #     res = 0
        #     for prev1 in range(val + 1):
        #         prev2 = nums[idx - 1] - prev1
        #         if prev2 < v2:
        #             break
        #         res += dfs(idx - 1, prev1)
        #         res %= MOD
        #     return res
        #
        # ans = 0
        # for val in range(nums[-1] + 1):
        #     ans += dfs(N - 1, val)
        #     ans %= MOD
        # return ans