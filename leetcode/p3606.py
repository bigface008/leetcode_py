# https://leetcode.com/problems/coupon-code-validator/?envType=daily-question&envId=2025-12-13
import string
from typing import List, Dict, Optional, Tuple


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        N = len(code)
        ans = []
        ch_set = set(string.ascii_letters + '_' + string.digits)
        business_set = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        for i in range(N):
            ci, bi, ii = code[i], businessLine[i], isActive[i]
            if not ci or not ii or bi not in business_set:
                continue
            valid_code = True
            for ch in ci:
                if ch not in ch_set:
                    valid_code = False
            if not valid_code:
                continue
            ans.append(i)
        ans.sort(key=lambda i : (business_set[businessLine[i]], code[i]))
        return [code[i] for i in ans]

        # def cmp(i1: int, i2: int) -> int:
        #     c1, b1 = code[i1], businessLine[i1]
        #     c2, b2 = code[i2], businessLine[i2]
        #     bs1 = business_set[b1]
        #     bs2 = business_set[b2]
        #     if bs1

