# https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2026-07-13
from typing import List, Dict, Set, Tuple


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        SL, SH = str(low), str(high)
        NL, NH = len(SL), len(SH)
        ans: List[int] = []

        def build_num(num_len: int, first_digit: int) -> Tuple[bool, int]:
            if first_digit + num_len - 1 > 9:
                return False, 0
            num = 0
            for i in range(num_len):
                num = num * 10 + first_digit + i
            return True, num

        # find the 1st number >= low
        for num_len in range(NL, NH + 1):
            start_first_digit = 1 if num_len != NL else int(SL[0])
            for first_digit in range(start_first_digit, 10):
                ok, num = build_num(num_len, first_digit)
                if not ok or num > high:
                    break
                if num >= low:
                    ans.append(num)
        return ans