from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/minimum-number-of-vertices-to-reach-all-nodes/description/
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for f, t in edges:
            in_degree[t] += 1
        ans = []
        for i, x in enumerate(in_degree):
            if x == 0:
                ans.append(i)
        return ans