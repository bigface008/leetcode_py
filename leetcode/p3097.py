# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/?envType=daily-question&envId=2025-01-17
import bisect
from typing import List
from math import inf

import utils


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = inf
        for i in range(N):
            curr = nums[i]
            if curr >= k:
                return 1
            j = i - 1
            while j >= 0 and (nums[j] | curr) < k and (nums[j] | curr) != nums[j]:
                nums[j] |= curr
                j -= 1
            if j >= 0 and (nums[j] | curr) >= k:
                ans = min(ans, i - j + 1)
        return ans if ans is not inf else -1


class Solution2:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = inf
        last_start = 0
        for i in range(N):
            curr = nums[i]
            j = bisect.bisect_left(range(last_start, i + 1), True, key=lambda idx: nums[idx] | curr < k) + last_start - 1
            for k in range(j, i + 1):
                if k >= 0:
                    nums[i] |= curr
            if j >= last_start:
                ans = min(i - j + 1, ans)
                last_start = j
        return ans



def check(nums: List[int], k: int, expect: int):
    output = Solution().minimumSubarrayLength(nums, k)
    utils.tst(f'nums={nums}, k={k}', output, expect)


if __name__ == '__main__':
    check([2, 1, 8], 10, 3)

    # N = len(nums)
    # all_or = 0
    # for x in nums:
    #     if x >= k:
    #         return 1
    #     all_or |= x
    # if all_or < k:
    #     return -1
    #
    # M = k.bit_length()
    # mp = [[]] * M
    # for i, x in enumerate(nums):
    #     for b in range(M):
    #         if x & (1 << b) != 0:
    #             mp[b].append(i)
    # return []

    # M = max(nums).bit_length()
    # mp = [[]] * M
    # for x in nums:
    #     for b in range(M):
    #         if x & (1 << b) != 0:
    #             mp[b].append()

    # ans = inf
    # for i in range(N):
    #     temp = 0
    #     for j in range(i, N):
    #         temp |= nums[j]
    #         if temp >= k:
    #             ans = min(ans, j - i + 1)
    #             break
    # return ans if ans is not inf else -1
