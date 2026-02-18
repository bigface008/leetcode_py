# https://leetcode.cn/problems/binary-number-with-alternating-bits/?envType=daily-question&envId=2026-02-18
from typing import Optional


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_digit: Optional[int] = None
        while n > 0:
            d = n & 1
            if last_digit is not None and d == last_digit:
                return False
            last_digit = d
            n >>= 1
        return True
