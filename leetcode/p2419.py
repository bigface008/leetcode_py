from typing import List

import utils


# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        max_val = max(nums)
        cnt = 1
        max_cnt = 1
        for i in range(1, N):
            x = nums[i]
            prev = nums[i - 1]
            if x == max_val:
                if prev == x:
                    cnt += 1
                    max_cnt = max(max_cnt, cnt)
                else:
                    cnt = 1
        return max_cnt


def tst(nums: List[int], expect: int):
    output = Solution().longestSubarray(nums)
    utils.tst(f'nums={nums}', output, expect)


if __name__ == '__main__':
    # tst([1, 2, 3, 3, 2, 2], 2)
    tst([323376, 323376, 323376, 323376, 323376, 323376, 323376, 75940, 75940], 7)
    # tst([1, 2, 3, 4], 1)
