# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/?envType=daily-question&envId=2024-12-11
import bisect
from typing import List

import utils


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            while x - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans


        # N = len(nums)
        # nums.sort()
        # start = 0
        # ans = 1
        #
        # def cmp2(idx: int) -> bool:
        #     res = nums[idx] > x + k
        #     return res
        #
        # for i, x in enumerate(nums):
        #     i1 = bisect.bisect_left(range(start, i), True, key=lambda idx: nums[idx] >= x - k) + start
        #     # i2 = bisect.bisect_left(range(i, N), True, key=cmp2) + i - 1
        #     i2 = bisect.bisect_left(range(i, N), True, key=lambda idx: nums[idx] > x + k) + i - 1
        #     # if i2 == N:
        #     #     i2 -= 1
        #     cnt = i2 - i1 + 1
        #     ans = max(ans, cnt)
        #     start = i1
        # return ans


def check(nums: List[int], k: int, expect: int):
    output = Solution().maximumBeauty(nums, k)
    utils.tst(f'{nums} {k}', output, expect)


if __name__ == '__main__':
    # check([4, 6, 1, 2], 2, 3)
    # check([12, 71], 10, 1)
    check([49, 26], 12, 2)
