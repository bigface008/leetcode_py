# https://leetcode.cn/problems/knight-dialer/description/?envType=daily-question&envId=2024-12-10
from functools import cache
from typing import Tuple


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        num2Sub = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

        @cache
        def dfs(num: int, times: int) -> int:
            if times == 1:
                return 1
            res = 0
            for node in num2Sub[num]:
                res += dfs(node, times - 1)
                res %= MOD
            return res

        return sum(dfs(x, n) for x in range(10)) % MOD
