from typing import List


# https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/description/
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        one_cnt = sum(nums)
        win_one_cnt = 0
        for i in range(one_cnt):
            if nums[i] == 1:
                win_one_cnt += 1
        max_win_one_cnt = win_one_cnt
        for i in range(one_cnt, N + one_cnt - 1):
            if nums[i % N] == 1:
                win_one_cnt += 1
            if nums[(i - one_cnt) % N] == 1:
                win_one_cnt -= 1
            max_win_one_cnt = max(win_one_cnt, max_win_one_cnt)
        return one_cnt - max_win_one_cnt
