# https://leetcode.com/problems/keep-multiplying-found-values-by-two/?envType=daily-question&envId=2025-11-19
from typing import List, Dict, Tuple, Optional
from math import log2


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        base = 0
        for x in nums:
            if x % original == 0:
                val = x // original
                if (val & (val - 1)) == 0:
                    base |= val
        offset = 0
        while (base & (1 << offset)) != 0:
            offset += 1
        if offset == 0:
            return original
        return original * (2 << offset)

        # res: Optional[int] = None
        # for x in nums:
        #     if x % original == 0:
        #         val = x // original
        #         if (val & (val - 1)) == 0:
        #             if res is None or x > res:
        #                 res = x
        # if res is None:
        #     return original
        # return res * 2


if __name__ == '__main__':
    Solution().findFinalValue([4,7,1,16,1,2,7,13], 1)