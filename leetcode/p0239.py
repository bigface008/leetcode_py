from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        window_cnt = N - k + 1
        ans = [0] * window_cnt
        mono_stk = []
        for i in range(k):
            while mono_stk and nums[mono_stk[-1]] < nums[i]:
                mono_stk.pop()
            mono_stk.append(i)
        ans[0] = nums[mono_stk[0]]
        for i in range(k, N):
            if mono_stk[0] == i - k:
                mono_stk.pop(0)
            while mono_stk and nums[mono_stk[-1]] < nums[i]:
                mono_stk.pop()
            mono_stk.append(i)
            ans[i - k + 1] = nums[mono_stk[0]]
        return ans
