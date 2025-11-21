# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/?envType=daily-question&envId=2025-11-17
from typing import List, Optional


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_pos: Optional[int] = None
        N = len(nums)
        for i in range(N):
            if nums[i] == 1:
                if last_pos is not None and i - last_pos < k + 1:
                    return False
                last_pos = i
        return True