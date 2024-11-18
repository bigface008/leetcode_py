import math
from functools import cache
from typing import List


import utils


# https://leetcode.cn/problems/count-the-number-of-inversions/description/?envType=daily-question&envId=2024-10-17
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        req = [-1] * n
        req[0] = 0
        max_cnt = 0
        for end, cnt in requirements:
            req[end] = cnt
            max_cnt = max(cnt, max_cnt)
        if req[0]:
            return 0

        dp = [[0] * (max_cnt + 1) for _ in range(n)]
        for j in range(max_cnt + 1):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(max_cnt + 1):
                cnt = req[i - 1]
                if cnt >= 0:
                    dp[i][j] = dp[i - 1][cnt] if cnt <= j <= i + cnt else 0
                else:
                    dp[i][j] = sum(dp[i - 1][j - k] for k in range(min(i, j) + 1)) % MOD
        return dp[n - 1][req[-1]]


        # MOD = pow(10, 9) + 7
        # req = [-1] * n
        # req[0] = 0
        # for end, cnt in requirements:
        #     req[end] = cnt
        # if req[0]:
        #     return 0
        #
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i == 0:
        #         return 1
        #     cnt = req[i - 1]
        #     if cnt >= 0:
        #         return dfs(i - 1, cnt) if cnt <= j <= i + cnt else 0
        #     else:
        #         return sum(dfs(i - 1, j - k) for k in range(min(i, j) + 1)) % MOD
        #
        # return dfs(n - 1, req[-1])




def tst(n: int, requirements: List[List[int]], expect: int):
    output = Solution().numberOfPermutations(n, requirements)
    utils.tst(f'n={n}, requirements={requirements}', output, expect)


if __name__ == '__main__':
    tst(3, [[2, 2], [0, 0]], 2)
    tst(3, [[2, 2], [1, 1], [0, 0]], 1)
