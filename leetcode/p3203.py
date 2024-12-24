# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/?envType=daily-question&envId=2024-12-24
from collections import defaultdict
from typing import List, Dict


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edges: List[List[int]]) -> int:
            N = len(edges) + 1
            g = [[] for _ in range(N)]
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)
            dia = 0

            def dfs(x: int, fa: int) -> int:
                nonlocal dia
                res = 0
                for y in g[x]:
                    if y != fa:
                        sub_len = dfs(y, x) + 1
                        dia = max(dia, res + sub_len)
                        res = max(res, sub_len)
                return res

            dfs(0, -1)
            return dia

        dia1 = diameter(edges1)
        dia2 = diameter(edges2)
        return max(dia1, dia2, (dia1 + 1) // 2 + (dia2 + 1) // 2 + 1)