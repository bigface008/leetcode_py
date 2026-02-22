# https://leetcode.cn/problems/binary-gap/?envType=daily-question&envId=2026-02-22
from math import inf


class Solution:
    def binaryGap(self, n: int) -> int:
        last_one_pos = -1
        i = 0
        ans = -inf
        while n > 0:
            d = n & 1
            if d == 1:
                if last_one_pos != -1:
                    ans = max(ans, i - last_one_pos)
                last_one_pos = i
            i += 1
            n >>= 1
        return ans if not (ans == -inf) else 0


if __name__ == "__main__":
    print(Solution().binaryGap(8))

