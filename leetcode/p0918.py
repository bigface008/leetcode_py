from itertools import accumulate
from typing import List
from functools import cache
from math import inf

import utils


# https://leetcode.cn/problems/maximum-sum-circular-subarray/description/
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        ans = nums[0]
        min_ans = min(0, nums[0])
        max_dp = ans
        min_dp = min_ans
        all_sum = nums[0]

        for i in range(1, N):
            x = nums[i]
            max_dp = max(max_dp, 0) + x
            min_dp = min(min_dp, 0) + x
            ans = max(ans, max_dp)
            min_ans = min(min_ans, min_dp)
            all_sum += x

        if min_ans == all_sum:
            return ans
        return max(ans, all_sum - min_ans)


# https://leetcode.cn/problems/maximum-sum-circular-subarray/
class Solution2:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        all_sum = sum(nums)
        all_max = max(nums)
        ans = all_max
        min_sum = 0

        def dfs1(i: int) -> int:
            nonlocal ans
            if i == 0:
                ans = max(ans, nums[0])
                return nums[0]

            curr = nums[i]
            prev = dfs1(i - 1)
            res = max(prev, 0) + curr
            ans = max(ans, res)
            return res

        def dfs2(i: int) -> int:
            nonlocal min_sum
            if i == 0:
                res = min(nums[0], 0)
                min_sum = min(min_sum, res)
                return res

            curr = nums[i]
            prev = dfs2(i - 1)
            res = min(prev, 0) + curr
            min_sum = min(min_sum, res)
            return res

        dfs1(N - 1)
        dfs2(N - 1)
        if min_sum == all_sum:
            return ans
        return max(ans, all_sum - min_sum)


def tst(nums: List[int], expect: int):
    output = Solution().maxSubarraySumCircular(nums)
    utils.tst(f'test {nums}', output, expect)


if __name__ == '__main__':
    # tst([5, -3, 5], 10)
    tst([9, -4, -7, 9], 18)
    # tst([-3, -2, -3], -2)
