# https://leetcode.com/problems/string-compression-iii/?envType=daily-question&envId=2024-11-04
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        N = len(word)
        i = 1
        cnt = 1
        prev_ch = word[0]
        while i <= N:
            ch = word[i] if i != N else ''
            if prev_ch == ch and cnt + 1 <= 9:
                cnt += 1
            else:
                comp += f'{cnt}{prev_ch}'
                cnt = 1
                prev_ch = ch
            i += 1
        return comp
