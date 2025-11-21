# https://leetcode.com/problems/tuple-with-same-product/?envType=daily-question&envId=2025-02-06
from collections import defaultdict
from typing import List

import utils


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # N = len(nums)
        # nums.sort()
        # left, right = 0, N - 1
        # prod_2_indices = defaultdict(list)
        # while left < right:
        #     pass

        N = len(nums)
        prod_2_indices = defaultdict(int)
        for i in range(N):
            a = nums[i]
            for j in range(i + 1, N):
                b = nums[j]
                prod_2_indices[a * b] += 1

        ans = 0
        for k, v in prod_2_indices.items():
            ans += v * (v - 1) // 2 * 8
        return ans


def check(nums: List[int], expect: int):
    output = Solution().tupleSameProduct(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    check([2, 3, 4, 6], 8)
