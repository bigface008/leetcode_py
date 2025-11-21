# https://leetcode.cn/problems/subsets-ii/?envType=daily-question&envId=2025-02-05
from typing import List

import utils


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        group = []

        def dfs(i: int):
            if i == N:
                ans.append(group.copy())
                return
            x = nums[i]
            group.append(nums[i])
            dfs(i + 1)
            group.pop()

            j = i + 1
            while j < N and nums[j] == x:
                j += 1
            dfs(j)

        dfs(0)
        return ans


def check(nums: List[int], expect: List[List[int]]):
    output = Solution().subsetsWithDup(nums)
    utils.tst(f'nums={nums} expect={expect}', output, expect)


if __name__ == '__main__':
    check([2, 2, 2], [[], [2], [2, 2], [2, 2, 2]])
    # check([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    # check([1, 2, 3], [[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]])
