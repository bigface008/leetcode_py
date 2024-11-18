import collections
from typing import List

import utils


# https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-i/?envType=daily-question&envId=2024-10-22
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mp = collections.Counter()
        ans = 0
        for i, hour in enumerate(hours):
            mod = hour % 24
            remain = 24 - mod
            if mod == 0:
                remain = 0
            if remain in mp:
                ans += mp[remain]
            mp[mod] += 1
        return ans


def tst(hours: List[int], expect: int):
    output = Solution().countCompleteDayPairs(hours)
    utils.tst(f'hours', output, expect)


if __name__ == '__main__':
    tst([12, 12, 30, 24, 24], 2)
    # tst([72, 48, 24, 3], 3)
