# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/?envType=daily-question&envId=2025-11-23
from typing import List, Dict, Tuple, Optional
from functools import cache
from math import inf

# x=0 j=0 0
# x=0 j=1 1
# x=0 j=2 2

# x=1 j=0 1
# x=1 j=1 2

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[-inf] * 3 for _ in range(N + 1)]
        dp[0][0] = 0
        for i, x in enumerate(nums):
            for j in range(3):
                dp[i + 1][j] = max(dp[i][j], dp[i][(j + x) % 3] + x)
        return dp[-1][0]

        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i < 0:
        #         return 0 if j == 0 else -inf
        #     return max(dfs(i - 1, j), dfs(i - 1, (j + nums[i]) % 3) + nums[i])
        # return dfs(len(nums) - 1, 0)



if __name__ == '__main__':
    Solution().maxSumDivThree([3,6,5,1,8])