# https://leetcode.com/problems/count-number-of-bad-pairs/?envType=daily-question&envId=2025-02-09
from typing import List
from collections import Counter

import utils


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        cnt = Counter()
        ans = N * (N - 1) // 2
        for i, x in enumerate(nums):
            ans -= cnt[x - i]
            cnt[x - i] += 1
        return ans


def check(nums: List[int], expect: int):
    output = Solution().countBadPairs(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    check([1, 2, 3, 4, 5], 0)
