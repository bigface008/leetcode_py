from typing import List
from functools import cache
from itertools import accumulate
from math import inf

import utils


# dfs(i) = sum(piles[i:]) - min(dfs(i + x))

# https://leetcode.com/problems/stone-game-ii/description/?envType=daily-question&envId=2024-08-20
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        sufSum = list(accumulate(piles[::-1], initial=0))[::-1]

        @cache
        def dfs(i: int, m: int) -> int:
            if i >= N:
                return 0
            next = -1
            for x in range(1, 2 * m + 1):
                tmp = dfs(i + x, max(x, m))
                if next == -1:
                    next = tmp
                else:
                    next = min(next, tmp)
            return sufSum[i] - next

        return dfs(0, 1)


def tst(piles: List[int], expect: int):
    output = Solution().stoneGameII(piles)
    utils.tst(f'stone game piles={piles}', output, expect)


if __name__ == '__main__':
    tst([2, 7, 9, 4, 4], 10)
    tst([1, 2, 3, 4, 5, 100], 104)
