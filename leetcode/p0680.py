# https://leetcode.cn/problems/valid-palindrome-ii/?envType=daily-question&envId=2025-02-03
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isValid(s: str) -> bool:
            N = len(s)
            for i in range(N // 2):
                if s[i] != s[N - i - 1]:
                    return False
            return True


        N = len(s)
        i, j = 0, N - 1
        while i < j:
            if s[i] != s[j]:
                return isValid(s[i + 1:j + 1]) or isValid(s[i:j])
            i += 1
            j -= 1
        return True
