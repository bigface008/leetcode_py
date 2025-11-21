# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
from typing import List

import utils


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        N = len(nums)
        valid_len = 0
        b1, b2 = 0, 0
        while valid_len < N:
            x = nums[valid_len]
            if x > pivot:
                valid_len += 1
            elif x < pivot:
                for i in range(valid_len, b1, -1):
                    nums[i] = nums[i - 1]
                nums[b1] = x
                b1 += 1
                b2 += 1
                valid_len += 1
            else:
                for i in range(valid_len, b2, -1):
                    nums[i] = nums[i - 1]
                nums[b2] = x
                b2 += 1
                valid_len += 1
        return nums


def check(nums: List[int], pivot: int, expect: List[int]):
    temp = nums.copy()
    output = Solution().pivotArray(nums, pivot)
    utils.tst(f'nums={temp} pivot={pivot}', output, expect)


if __name__ == '__main__':
    check([9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14])

# pivot = 1
# l 0
# r 4
# i 1
# 1 3 1 0 5 4 2
