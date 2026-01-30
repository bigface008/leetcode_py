# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description/?envType=daily-question&envId=2026-01-30
import heapq
from collections import defaultdict
from typing import List, Dict, Tuple, Set
from math import inf
from functools import cache


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        N, M = len(source), len(original)
        graph: Dict[str, Dict[str, int]] = defaultdict(dict)
        ch_to_origin_mp: Dict[str, Set[str]] = defaultdict(set)
        for w1, w2, c in zip(original, changed, cost):
            ch_to_origin_mp[w1[0]].add(w1)
            if w2 in graph[w1]:
                graph[w1][w2] = min(graph[w1][w2], c)
            else:
                graph[w1][w2] = c
        min_convert_cost_mp: Dict[str, int] = dict()

        def get_convert_cost(w1: str, w2: str) -> int:
            if w1 == w2:
                return 0
            nonlocal min_convert_cost_mp
            if (w1 + '.' + w2) in min_convert_cost_mp:
                return min_convert_cost_mp[w1 + '.' + w2]
            pq = [(0, w1)]  # cost, word
            min_dist: Dict[str, int] = {w1: 0}
            while pq:
                dist, word = pq[0]
                heapq.heappop(pq)
                if dist > min_dist.get(word, inf):
                    continue
                for neighbor, neighbor_cost in graph[word].items():
                    neighbor_dist = neighbor_cost + dist
                    if neighbor_dist < min_dist.get(neighbor, inf):
                        min_dist[neighbor] = neighbor_dist
                        heapq.heappush(pq, (neighbor_dist, neighbor))
            for word, dist in min_dist.items():
                min_convert_cost_mp[w1 + '.' + word] = min(dist, min_convert_cost_mp.get(word, inf))
            if w2 not in min_dist:
                return inf
            return min_dist[w2]

        @cache
        def dfs(source_idx: int) -> int:
            if source_idx == N:
                return 0
            res = inf
            if source[source_idx] == target[source_idx]:
                res = min(res, dfs(source_idx + 1))
            for w1 in ch_to_origin_mp[source[source_idx]]:
                WL = len(w1)
                if WL > N - source_idx:
                    continue
                if source[source_idx:source_idx + WL] == w1:
                    convert_cost = get_convert_cost(w1, target[source_idx:source_idx + WL])
                    if convert_cost is inf:
                        continue
                    sub_arr_cost = dfs(source_idx + WL)
                    if sub_arr_cost is inf:
                        continue
                    res = min(res, convert_cost + sub_arr_cost)
            return res

        ans = dfs(0)
        return ans if ans is not inf else -1


if __name__ == '__main__':
    # print(Solution().minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"],
    #                              [2, 5, 5, 1, 2, 20]))
    # print(Solution().minimumCost("abcdefgh", "acdeeghh", ["bcd", "fgh", "thh"], ["cde", "thh", "ghh"], [1, 3, 5]))
    # print(Solution().minimumCost("ahhebhhbbhbebaeehbbh", "hbebaeebebhabeehahhb",
    #                              ["a", "h", "h", "b", "b", "e", "a", "e", "h", "b"],
    #                              ["h", "b", "e", "a", "e", "a", "e", "h", "a", "h"], [4, 8, 2, 8, 9, 9, 9, 8, 9, 6]))
    print(Solution().minimumCost("aaaddcaaccbabaaccbabbaadcccadbaacbddbaccabddbdbaaddbbacbddddbbdbccaadcaccacdbcbddbacabadaaccbadbbdbc",
                                 "abaddcabcdbabcbadcaccaadabbadddbcacaaabdabbdcbbdbcbaaabbbcddcbddcbccadacddcbdcbacadbbadbdabcbadbbdac",
                                 ["ddddb","dccbb","dadac","dbdbb","ddbacabadaac","bcbccdcadabd","dacabcdaacca","dcdadacacbbd","dcccadbaacbddbacc","dcdcbccdccdbaaaac","bbbcccdbcdcadaabc","bccaadcaccacdb","bbcabcbcbaddbd","dbadadaddcddad","badaddbcddacca","bc","da","cb","ddbdbaaddbbac","dbcadcdbabddd","abdadacbbbcca","adaaabcabdbcc","caaccbabaaccbabba","abaadddbaaccbbacc","bbddaaadcbccccbac","cdbdbddaadbbbdbdd","bcbdaabaddbdcdcaa","aa","cb","dd"],
                                 ["dccbb","dadac","dbdbb","bcddc","bcbccdcadabd","dacabcdaacca","dcdadacacbbd","acadbbadbdab","dcdcbccdccdbaaaac","bbbcccdbcdcadaabc","dabbadddbcacaaabd","bbcabcbcbaddbd","dbadadaddcddad","badaddbcddacca","dcbccadacddcbd","da","cb","ac","dbcadcdbabddd","abdadacbbbcca","adaaabcabdbcc","bdcbbdbcbaaab","abaadddbaaccbbacc","bbddaaadcbccccbac","cdbdbddaadbbbdbdd","bcbdaabaddbdcdcaa","cabcdbabcbadcacca","cb","dd","ba"],
                                 [67,56,64,83,100,73,95,97,100,98,20,92,58,70,95,77,95,93,69,92,77,53,96,68,83,96,93,64,81,100]))
