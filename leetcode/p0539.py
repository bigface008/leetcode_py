from typing import List

import utils


# https://leetcode.com/problems/minimum-time-difference/description/?envType=daily-question&envId=2024-09-16
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        N = len(timePoints)
        MOD = 24 * 60
        nums = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        nums.sort()
        ans = MOD - nums[-1] + nums[0]
        for i in range(N - 1):
            ans = min(ans, nums[i + 1] - nums[i])
        return ans


def tst(timePoints: List[int], expect: int):
    output = Solution().findMinDifference(timePoints)
    utils.tst(f'findMinDifference timePoints={timePoints}', output, expect)


if __name__ == '__main__':
    tst(["23:59", "00:00"], 1)
