# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/?envType=daily-question&envId=2025-02-09
from typing import List

import utils


# 1, 2, 2, 2, 3, 3, 3, 4, 5
#


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        same_cnt = 0
        # i = 0
        j = 0
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                same_cnt += 1
            else:
                same_cnt = 1
            if same_cnt <= 2:
                nums[j] = nums[i]
                j += 1
        return j


def check(nums: List[int], expect: int):
    output = Solution().removeDuplicates(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    check([1, 1, 1, 2, 2, 3], 5)
