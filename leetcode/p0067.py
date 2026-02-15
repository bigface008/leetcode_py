# https://leetcode.cn/problems/add-binary/?envType=daily-question&envId=2026-02-15
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res: List[str] = []
        i = 0
        over = 0
        while i < len(a) and i < len(b):
            va = int(a[-(i + 1)])
            vb = int(b[-(i + 1)])
            v = va + vb + over
            over = v >> 1
            res.append(str(v & 1))
            i += 1
        while i < len(a):
            v = int(a[-(i + 1)]) + over
            over = v >> 1
            res.append(str(v & 1))
            i += 1
        while i < len(b):
            v = int(b[-(i + 1)]) + over
            over = v >> 1
            res.append(str(v & 1))
            i += 1
        if over:
            res.append('1')
        return ''.join(reversed(res))

