from typing import List
from math import inf

import utils


# https://leetcode.cn/problems/smallest-range-ii/?envType=daily-question&envId=2024-10-21
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N == 1:
            return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(N - 1):
            mn = min(nums[i + 1] - k, nums[0] + k)
            mx = max(nums[i] + k, nums[-1] - k)
            ans = min(ans, mx - mn)
        return ans


def tst(nums: List[int], k: int, expect: int):
    output = Solution().smallestRangeII(nums, k)
    utils.tst(f'smallest range nums={nums} k={k}', output, expect)


if __name__ == '__main__':
    tst([1, 3, 6], 3, 3)
