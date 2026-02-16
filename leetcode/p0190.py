# https://leetcode.cn/problems/reverse-bits/?envType=daily-question&envId=2026-02-16
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += n & 1
            ans <<= 1
            if i != 31:
                n >>= 1
        return ans