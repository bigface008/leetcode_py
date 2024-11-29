from itertools import accumulate
from typing import List
from functools import cache

import utils

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)
        M = max(nums) + 1
        MOD = pow(10, 9) + 7
        dp = [[0] * M for _ in range(N)]
        for v1 in range(nums[0] + 1):
            dp[0][v1] = 1
        for idx in range(1, N):
            pre_sum = list(accumulate(dp[idx - 1]))
            for v1 in range(nums[idx] + 1):
                max_k = v1 + min(0, nums[idx - 1] - nums[idx])
                dp[idx][v1] = pre_sum[max_k] % MOD if max_k >= 0 else 0
        return sum(dp[-1][:nums[-1] + 1]) % MOD


class Solution3:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7
        ans = 0
        dp = [[0] * (nums[-1] + 1) for _ in range(N)]
        for v1 in range(0, nums[-1] + 1):
            for idx in range(N):
                v2 = nums[idx] - v1
                if v1 < 0 or v2 < 0:
                    continue
                if idx == 0:
                    dp[idx][v1] = 1
                    continue
                res = 0
                for prev1 in range(0, v1 + 1):
                    prev2 = nums[idx - 1] - prev1
                    if prev2 < v2:
                        continue
                    res += dp[idx - 1][prev1] % MOD
                res %= MOD
                dp[idx][v1] = res
            ans += dp[N - 1][v1]
            ans %= MOD
        return ans


class Solution2:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7
        ans = 0

        @cache
        def dfs(idx: int, v1: int) -> int:
            v2 = nums[idx] - v1
            if v1 < 0 or v2 < 0:
                return 0
            if idx == 0:
                return 1
            res = 0
            for prev1 in range(0, v1 + 1):
                prev2 = nums[idx - 1] - prev1
                if prev2 < v2:
                    continue
                res += dfs(idx - 1, prev1) % MOD
            res %= MOD
            return res

        for v1 in range(0, nums[-1] + 1):
            ans += dfs(N - 1, v1)
            ans %= MOD
        return ans


def tst(nums: List[int], expect: int):
    output = Solution().countOfPairs(nums)
    utils.tst(f'count of pairs nums={nums}', output, expect)


if __name__ == '__main__':
    tst([2, 3, 2], 4)
