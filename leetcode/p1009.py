# https://leetcode.cn/problems/complement-of-base-10-integer/?envType=daily-question&envId=2026-03-11
from typing import List

from nltk.corpus import reuters


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        offset = 0
        ans = 0
        while n:
            d = n & 1
            ans += (1 - d) << offset
            n >>= 1
            offset += 1
        return ans


if __name__ == "__main__":
    print(Solution().bitwiseComplement(5))