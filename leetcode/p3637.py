# https://leetcode.com/problems/trionic-array-i/description/?envType=daily-question&envId=2026-02-03
from typing import List, Dict, Tuple, Optional


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0
        N = len(nums)
        p_idx: Optional[int] = None
        q_idx: Optional[int] = None
        while i < N - 1:
            if nums[i] >= nums[i + 1]:
                p_idx = i
                break
            i += 1
        if p_idx is None or p_idx == 0:
            return False
        while i < N - 1:
            if nums[i] <= nums[i + 1]:
                q_idx = i
                break
            i += 1
        if q_idx is None or q_idx == N - 1:
            return False
        while i < N - 1:
            if nums[i] >= nums[i + 1]:
                return False
            i += 1
        return True


if __name__ == '__main__':
    print(Solution().isTrionic([2, 1, 3]))
