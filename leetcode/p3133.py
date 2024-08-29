

# https://leetcode.cn/problems/minimum-array-end/?envType=daily-question&envId=2024-08-22
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        i, j = 0, 0
        ans = x
        while n >> j:
            if (x >> i) & 1 == 0:
                ans |= ((n >> j) & 1) << i
                j += 1
            i += 1
        return ans
