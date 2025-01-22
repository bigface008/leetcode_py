# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/?envType=daily-question&envId=2025-01-16
from typing import List
from math import inf

import utils


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = inf
        for i in range(N):
            temp = 0
            for j in range(i, N):
                temp |= nums[j]
                if temp >= k:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans is not inf else -1


def check(nums: List[int], k: int, expect: int):
    output = Solution().minimumSubarrayLength(nums, k)
    utils.tst(f'nums={nums}, k={k}', output, expect)


if __name__ == '__main__':
    check([2, 1, 8], 10, 3)
