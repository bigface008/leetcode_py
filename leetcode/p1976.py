# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/description/
from collections import defaultdict
from typing import List
from math import inf
import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        graph = [[] for _ in range(n)]
        for (u, v, t) in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        dist = [inf] * n
        paths_cnt = [0] * n
        hp = [(0, 0)]
        dist[0] = 0
        paths_cnt[0] = 1
        while hp:
            time, node = heapq.heappop(hp)
            if time > dist[node]:
                continue
            for (sub_node, time_1) in graph[node]:
                new_time = time + time_1
                if new_time < dist[sub_node]:
                    dist[sub_node] = new_time
                    paths_cnt[sub_node] = paths_cnt[node]
                    heapq.heappush(hp, (new_time, sub_node))
                elif new_time == dist[sub_node]:
                    paths_cnt[sub_node] += paths_cnt[node] % MOD
        return paths_cnt[-1]
