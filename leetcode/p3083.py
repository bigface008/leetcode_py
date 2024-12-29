# https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/?envType=daily-question&envId=2024-12-26
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)
        seen = set()
        for i in range(1, N):
            ch1 = s[i]
            ch0 = s[i - 1]
            seen.add(ch0 + ch1)
            if (ch1 + ch0) in seen:
                return True
        return False