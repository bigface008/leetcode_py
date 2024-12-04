# https://leetcode.cn/problems/partition-equal-subset-sum/
from itertools import accumulate
from typing import List
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        all_sum = sum(nums)
        if all_sum % 2 != 0:
            return False
        half = all_sum // 2

        @cache
        def dfs(i: int, cap: int) -> bool:
            if cap < 0:
                return False
            if i == 0:
                return cap == 0 or cap == nums[0]
            x = nums[i]
            return dfs(i - 1, cap - x) or dfs(i - 1, cap)

        return dfs(N - 1, half)



# if __name__ == '__main__':
#     print(list(accumulate([1, 2, 3])))
#     print(list(accumulate([1, 2, 3], initial=0)))
