from collections import defaultdict
from typing import List


# https://leetcode.com/problems/find-the-town-judge/
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * n
        out_degree = [0] * n
        for a, b in trust:
            in_degree[b - 1] += 1
            out_degree[a - 1] += 1
        for i in range(n):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        return -1


