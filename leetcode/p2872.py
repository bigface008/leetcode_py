# https://leetcode.com/problems/maximum-number-of-k-divisible-components/?envType=daily-question&envId=2024-12-21
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        subtree_sum = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = 0

        def dfs1(node: int, parent: int) -> int:
            nonlocal ans
            res = values[node]
            for u in graph[node]:
                if u != parent:
                    res += dfs1(u, node)
            subtree_sum[node] = res
            ans += res % k == 0
            return res

        dfs1(0, -1)
        return ans