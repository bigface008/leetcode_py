from typing import List
from math import inf
from functools import cache
from collections import Counter

from sqlalchemy.sql.coercions import expect

import utils


# https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        nums = sorted(cnt.keys())
        N = len(nums)

        @cache
        def dfs(idx: int) -> int:
            if idx < 0:
                return 0
            i = idx - 1
            curr = nums[idx]
            found = False
            while i >= 0:
                if nums[i] < curr - 2:
                    found = True
                    break
                i -= 1
            return max(dfs(idx - 1), dfs(i) + curr * cnt[curr])

        return dfs(N - 1)


def tst(power: List[int], expect: int):
    output = Solution().maximumTotalDamage(power)
    utils.tst(f'power={power}', output, expect)


if __name__ == '__main__':
    tst([1, 1, 3, 4], 6)
