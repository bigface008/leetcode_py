# https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=daily-question&envId=2026-03-06
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        N = len(s)
        last_one = -1
        for i, ch in enumerate(s):
            if ch == '1':
                if last_one != -1 and i - 1 != last_one:
                    return False
                last_one = i
        return True

