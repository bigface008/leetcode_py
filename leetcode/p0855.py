# https://leetcode.cn/problems/exam-room/?envType=daily-question&envId=2024-12-23
import heapq
from typing import List, Tuple
from sortedcontainers import SortedList


class ExamRoom:

    def __init__(self, n: int):
        def dist(x: Tuple[int, int]) -> int:
            l, r = x
            return r - l - 1 if l == -1 or r == n else (r - l) // 2

        self.sl = SortedList(key=lambda x: (-dist(x), x[0]))
        self.N = n
        self.left = dict()
        self.right = dict()
        self.add((-1, n))

    def seat(self) -> int:
        s = self.sl[0]
        p = (s[0] + s[1]) // 2
        if s[0] == -1:
            p = 0
        elif s[1] == self.N:
            p = self.N - 1
        self.delete(s)
        self.add((s[0], p))
        self.add((p, s[1]))
        return p

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))

    def add(self, s: Tuple[int, int]):
        self.sl.add(s)
        self.left[s[1]] = s[0]
        self.right[s[0]] = s[1]

    def delete(self, s: Tuple[int, int]):
        self.sl.remove(s)
        self.left.pop(s[1])
        self.right.pop(s[0])