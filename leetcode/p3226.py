# https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/?envType=daily-question&envId=2024-11-02
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        while n > 0 or k > 0:
            dn = n & 1
            dk = k & 1
            if dn == 1 and dk == 0:
                ans += 1
            elif dn == 0 and dk == 1:
                return -1
            n >>= 1
            k >>= 1
        return ans
