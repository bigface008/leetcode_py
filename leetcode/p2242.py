import heapq
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/maximum-score-of-a-node-sequence/
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((scores[v], v))
            graph[v].append((scores[u], u))
        for i, info in graph.items():
            if len(info) > 3:
                graph[i] = heapq.nlargest(3, info)

        ans = -1
        for x, y in edges:
            for score_a, a in graph[x]:
                for score_b, b in graph[y]:
                    if y != a and a != b and b != x:
                        ans = max(ans, score_a + scores[x] + scores[y] + score_b)
        return ans

    # def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
    #     graph = defaultdict(list)
    #     for u, v in edges:
    #         graph[u].append((scores[v], v))
    #         graph[v].append((scores[u], u))
    #     for i, info in graph.items():
    #         if len(info) > 3:
    #             graph[i] = heapq.nlargest(3, info)
    #
    #     ans = -1
    #     for u, v in edges:
    #         for score_a, a in graph[u]:
    #             for score_b, b in graph[v]:
    #                 if u != a != b != v:
    #                     ans = max(ans, score_a + scores[u] + scores[v] + score_b)
    #     return ans