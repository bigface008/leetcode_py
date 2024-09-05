# https://leetcode.cn/problems/clear-digits/?envType=daily-question&envId=2024-09-05
class Solution:
    def clearDigits(self, s: str) -> str:
        ls = list(s)
        N = len(s)

        def findNum() -> int:
            for i, s in enumerate(ls):
                if s.isnumeric():
                    return i
            return -1

        idx = findNum()
        while idx != -1:
            tgt = -1
            for i in range(idx - 1, -1, -1):
                if not ls[i].isnumeric():
                    tgt = i
                    break
            ls.pop(idx)
            if tgt != -1:
                ls.pop(tgt)
            idx = findNum()
        return ''.join(ls)
