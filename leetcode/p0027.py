# https://leetcode.cn/problems/remove-element/
from typing import List, Dict, Optional, Tuple


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stk_size = 0
        for i, x in enumerate(nums):
            if x != val:
                nums[stk_size] = x
                stk_size += 1
        return stk_size