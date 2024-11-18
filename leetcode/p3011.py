from typing import List


# https://leetcode.com/problems/find-if-array-can-be-sorted/?envType=daily-question&envId=2024-11-06
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        cur_set_bits = nums[0].bit_count()
        cur_max = nums[0]
        cur_min = nums[0]
        range_arr = []
        for i in range(1, N):
            x = nums[i]
            cnt = x.bit_count()
            if cnt == cur_set_bits:
                cur_max = max(x, cur_max)
                cur_min = min(x, cur_min)
            else:
                range_arr.append((cur_min, cur_max))
                cur_set_bits = cnt
                cur_max = x
                cur_min = x
        range_arr.append((cur_min, cur_max))
        for i in range(1, len(range_arr)):
            if range_arr[i][0] < range_arr[i - 1][1]:
                return False
        return True

