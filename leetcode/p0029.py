from typing import List
import bisect


# https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        elif divisor == -1:
            if dividend == -(1 << 31):
                return (1 << 31) - 1
            return -dividend
        up, down = abs(dividend), abs(divisor)

        def div(a: int, b: int) -> int:
            if a < b:
                return 0
            if b == 1:
                return a
            sb = b
            res = 1
            while (sb + sb) <= a:
                sb += sb
                res += res
            return res + div(a - sb, b)

        res = div(up, down)
        if (dividend > 0 > divisor) or (dividend < 0 < divisor):
            return -res
        else:
            return res