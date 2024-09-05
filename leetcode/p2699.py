from collections import defaultdict
from typing import List
from math import inf


# https://leetcode.com/problems/modify-graph-edge-weights/description/?envType=daily-question&envId=2024-08-30
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:
        graph = defaultdict(set)
        for i, (x, y, _) in enumerate(edges):
            graph[x].add((y, i))
            graph[y].add((x, i))

        dist = [[inf, inf] for _ in range(n)]
        dist[source] = [0, 0]

        def dj(k: int):
            visited = [False] * n
            while True:
                x = -1
                for y, (vis, d) in enumerate(zip(visited, dist)):
                    if not vis and (x < 0 or d[k] < dist[x][k]):
                        x = y
                if x == destination:
                    return
                visited[x] = True
                for y, eid in graph[x]:
                    wt = edges[eid][2]
                    if wt == -1:
                        wt = 1
                    if k == 1 and edges[eid][2] == -1:
                        w = delta + dist[y][0] - dist[x][1]
                        if w > wt:
                            edges[eid][2] = wt = w
                    dist[y][k] = min(dist[y][k], dist[x][k] + wt)

        dj(0)
        delta = target - dist[destination][0]
        if delta < 0:
            return []

        dj(1)
        if dist[destination][1] < target:
            return []

        for e in edges:
            if e[2] == -1:
                e[2] = 1
        return edges
