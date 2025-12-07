# https://leetcode.cn/problems/maximum-running-time-of-n-computers/description/?envType=daily-question&envId=2025-12-01
from typing import List, Dict, Optional, Tuple


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # l, r = 0, sum(batteries) // n + 1
        # while l + 1 < r:
        #     x = (l + r) // 2
        #     if n * x <= sum(min(b, x) for b in batteries):
        #         l = x
        #     else:
        #         r = x
        # return l

        end = sum(batteries) // n + 1
        start = 1
        while start < end:
            mid = (start + end) // 2
            if n * mid > sum(min(b, mid) for b in batteries):
                end = mid
            else:
                start = mid + 1
        if n * start <= sum(min(b, start) for b in batteries):
            return start
        else:
            return start - 1


if __name__ == '__main__':
    print(Solution().maxRunTime(1, [1000000000]))
