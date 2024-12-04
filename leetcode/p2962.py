# https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/
from typing import List

import utils


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        mx = max(nums)
        left = 0
        mx_cnt = 0
        ans = 0
        for right in range(N):
            curr = nums[right]
            if curr == mx:
                mx_cnt += 1
            while mx_cnt > k or (mx_cnt == k and nums[left] != mx):
                if nums[left] == mx:
                    mx_cnt -= 1
                left += 1
            if mx_cnt == k:
                ans += left + 1
        return ans


def tst(nums: List[int], k: int, expect: int):
    output = Solution().countSubarrays(nums, k)
    utils.tst(f'nums={nums} k={k}', output, expect)


if __name__ == '__main__':
    tst([1, 3, 2, 3, 3], 2, 6)
