# https://leetcode.cn/problems/find-the-key-of-the-numbers/?envType=daily-question&envId=2025-01-11
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def to_str(n: int) -> str:
            s = str(n)
            if len(s) < 4:
                s = (4 - len(s)) * '0' + s
            return s

        s1, s2, s3 = to_str(num1), to_str(num2), to_str(num3)
        ans = 0
        for i in range(4):
            ans += min(int(ch) for ch in (s1[i], s2[i], s3[i])) * pow(10, 3 - i)
        return ans

