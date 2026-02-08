# https://leetcode.com/problems/minimum-removals-to-balance-array/?envType=daily-question&envId=2026-02-06
from typing import List
from math import inf


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        left = 0
        mx_remain = 0
        for i, mx in enumerate(nums):
            while nums[left] * k < mx:
                left += 1
            mx_remain = max(mx_remain, i - left + 1)
        return N - mx_remain

        # nums.sort()
        # N = len(nums)
        # ans = inf
        # start, end = 1, N
        # for i, x in enumerate(nums):
        #     limit = x * k
        #     while start < end:
        #         mid = (start + end) // 2
        #         if nums[mid] <= limit:
        #             start = mid + 1
        #         else:
        #             end = mid
        #     if start == N or nums[start] > limit:
        #         start -= 1
        #     ans = min(ans, N - (start - i + 1))
        #     if start == N - 1:
        #         break
        # return ans


if __name__ == "__main__":
    # print(Solution().minRemoval([1, 6, 2, 9], 3))
    print(Solution().minRemoval([4, 6], 2))
