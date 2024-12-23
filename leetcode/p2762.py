# https://leetcode.com/problems/continuous-subarrays/description/?envType=daily-question&envId=2024-12-14
import heapq
from collections import defaultdict, Counter, deque
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        max_stk = deque()
        min_stk = deque()
        for right, x in enumerate(nums):
            while max_stk and nums[max_stk[-1]] <= x:
                max_stk.pop()
            max_stk.append(right)
            while min_stk and nums[min_stk[-1]] >= x:
                min_stk.pop()
            min_stk.append(right)

            while nums[max_stk[0]] - nums[min_stk[0]] > 2:
                left += 1
                if max_stk[0] < left:
                    max_stk.popleft()
                if min_stk[0] < left:
                    min_stk.popleft()

            ans += right - left + 1
        return ans


        # num_cnt = Counter()
        # left = 0
        # ans = 0
        # for right, x in enumerate(nums):
        #     num_cnt[x] += 1
        #     while max(num_cnt) - min(num_cnt) > 2:
        #         y = nums[left]
        #         num_cnt[y] -= 1
        #         if num_cnt[y] == 0:
        #             del num_cnt[y]
        #         left += 1
        #     ans += right - left + 1
        # return ans