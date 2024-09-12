from typing import List
from math import inf

import utils


# https://leetcode.com/problems/3sum-closest/description/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        min_diff = inf
        N = len(nums)
        nums.sort()
        for i in range(N - 2):
            x = nums[i]
            if i > 0 and nums[i - 1] == x:
                continue
            j, k = i + 1, N - 1
            less_cnt = 0
            more_cnt = 0
            while j < k:
                y, z = nums[j], nums[k]
                curr_sum = x + y + z
                curr_diff = abs(curr_sum - target)
                if curr_sum > target:
                    more_cnt += 1
                    k -= 1
                elif curr_sum < target:
                    less_cnt += 1
                    j += 1
                elif curr_sum == target:
                    return target
                if curr_diff < min_diff:
                    ans = curr_sum
                    min_diff = curr_diff
        return ans


def tst(nums: List[int], target: int, expect: int):
    output = Solution().threeSumClosest(nums, target)
    utils.tst(f'3sum closest nums={nums} target={target}', output, expect)


if __name__ == '__main__':
    # tst([-1, 2, 1, -4], 1, 2)
    # tst([4, 0, 5, -5, 3, 3, 0, -4, -5], -2, -2)
    tst([4, 0, 5, -5, 3, 3, 0, -4, -5], -2, -2)
