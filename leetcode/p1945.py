# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/?envType=daily-question&envId=2024-09-03
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        ss = 0
        num = ''
        for ch in s:
            n = ord(ch) - ord('a') + 1
            num += str(n)
        for _ in range(k):
            digit = 0
            for ch in num:
                digit += int(ch)
            num = str(digit)
        return int(num)
