# https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2026-01-29
import heapq
from collections import defaultdict
from typing import List, Dict, Tuple
from math import inf


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph: Dict[int, Dict[int, int]] = defaultdict(dict)
        for ch1, ch2, w in zip(original, changed, cost):
            v1, v2 = ord(ch1) - ord('a'), ord(ch2) - ord('a')
            graph[v1][v2] = min(w, graph[v1][v2]) if v2 in graph[v1] else w

        known_min_cost: Dict[str, int] = dict()
        ans = 0
        for ch1, ch2 in zip(source, target):
            if (ch1 + ch2) in known_min_cost:
                ans += known_min_cost[ch1 + ch2]
                continue
            v1, v2 = ord(ch1) - ord('a'), ord(ch2) - ord('a')
            min_dist = [inf] * 26
            min_dist[v1] = 0
            pq = [(0, v1)]  # cost, ch_idx
            while pq:
                dist, ch_idx = pq[0]
                heapq.heappop(pq)
                if dist > min_dist[ch_idx]:
                    continue
                if ch_idx not in graph:
                    continue
                for next_ch_idx, w in graph[ch_idx].items():
                    dist_next_ch = w + dist
                    if dist_next_ch < min_dist[next_ch_idx]:
                        min_dist[next_ch_idx] = dist_next_ch
                        heapq.heappush(pq, (dist_next_ch, next_ch_idx))
            if min_dist[v2] is inf:
                return -1
            ans += min_dist[v2]
            for ch_idx, mn in enumerate(min_dist):
                if mn is not inf:
                    known_min_cost[ch1 + chr(ch_idx + ord('a'))] = mn
        return ans


if __name__ == '__main__':
    print(Solution().minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"],
                                 [2, 5, 5, 1, 2, 20]))
