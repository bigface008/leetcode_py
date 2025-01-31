# https://leetcode.cn/problems/jump-game-ii/?envType=daily-question&envId=2025-01-27
from typing import List
from math import inf
from functools import cache

import utils


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_bridge = 0
        next_bridge = 0
        for i in range(len(nums) - 2):
            next_bridge = max(next_bridge, i + nums[i])
            if i == cur_bridge:
                cur_bridge = next_bridge
                ans += 1
        return ans


class Solution3:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        for i in range(1, N):
            if i <= nums[0]:
                dp[i] = 1
                continue
            res = inf
            for j in range(i - 1, -1, -1):
                if j + nums[j] >= i:
                    res = min(res, dp[j] + 1)
            dp[i] = res
        return dp[-1]


class Solution2:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dfs(i: int) -> int:
            if i == 0:
                print(f'i={i} ans={0}')
                return 0
            if i <= nums[0]:
                print(f'i={i} ans={1}')
                return 1
            ans = inf
            for j in range(i - 1, -1, -1):
                if j + nums[j] >= i:
                    ans = min(ans, dfs(j) + 1)
            print(f'i={i} ans={ans}')
            return ans

        return dfs(N - 1)


def check(nums: List[int], expect: int):
    output = Solution().jump(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    check([2, 3, 1, 1, 4], 2)
