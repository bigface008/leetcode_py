# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/?envType=daily-question&envId=2026-01-03
from functools import cache


# 0 4 8
# 1 5 9
# 2 6 10
# 3 7 11


# 0->4,5,7,8,9
# 1->4,6,7,8
# 2->4,5,8,9,11
# 3->....



# dfs(i, plan) =
# if plan = 0:
#
#

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [[0, 0] for _ in range(n)]
        dp[-1][0] = 1
        dp[-1][1] = 1
        for i in range(n - 2, -1, -1):
            dp[i][0] = (3 * dp[i + 1][0] + 2 * dp[i + 1][1]) % MOD
            dp[i][1] = (2 * dp[i + 1][0] + 2 * dp[i + 1][1]) % MOD
        return (6 * dp[0][0] + 6 * dp[0][1]) % MOD


        # MOD = pow(10, 9) + 7
        # @cache
        # def dfs(i: int, plan: int) -> int:
        #     if i == n - 1:
        #         return 1
        #     if plan == 0:
        #         return (3 * dfs(i + 1, 0) + 2 * dfs(i + 1, 1)) % MOD
        #     else:
        #         return (2 * dfs(i + 1, 0) + 2 * dfs(i + 1, 1)) % MOD
        # return (6 * dfs(0, 0) + 6 * dfs(0, 1)) % MOD


if __name__ == '__main__':
    print(Solution().numOfWays(2))
    print(Solution().numOfWays(3))
    print(Solution().numOfWays(7))
    print(Solution().numOfWays(5000))

