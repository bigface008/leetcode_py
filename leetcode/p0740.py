from collections import defaultdict
from typing import List, Tuple
from functools import cache

import utils


# https://leetcode.com/problems/delete-and-earn/
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_to_cnt: defaultdict[int, int] = defaultdict(int)
        for n in nums:
            num_to_cnt[n] += 1
        counts = []
        nums = list(num_to_cnt.keys())
        N = len(nums)
        nums.sort()
        for n in nums:
            counts.append(num_to_cnt[n])

        @cache
        def dfs(i: int) -> Tuple[int, int]:
            if i < 0:
                return 0, 0
            if i == 0:
                return nums[0] * counts[0], 0
            r1, r2 = 0, 0
            if nums[i] == nums[i - 1] + 1:
                r1 = counts[i] * nums[i] + max(dfs(i - 2))
            else:
                r1 = counts[i] * nums[i] + max(dfs(i - 1))
            r2 = max(dfs(i - 1))
            return r1, r2

        return max(dfs(N - 1))


def tst(nums: List[int], expect: int):
    output = Solution().deleteAndEarn(nums)
    utils.tst(f'delete & earn nums={nums}', output, expect)


if __name__ == '__main__':
    tst([3, 4, 2], 6)
    tst([2, 2, 3, 3, 3, 4], 9)
