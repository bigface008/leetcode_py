# https://leetcode.cn/problems/find-all-people-with-secret/
from collections import defaultdict
from typing import List, Set, Dict

from scipy.stats import expon

import utils


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        visited: Set[int] = set()
        visited.add(0)
        visited.add(firstPerson)

        M = len(meetings)
        time_to_graph: Dict[int, Dict[int, List[int]]] = defaultdict(dict)
        for x, y, time in meetings:
            if x not in time_to_graph[time]:
                time_to_graph[time][x] = []
            time_to_graph[time][x].append(y)
            if y not in time_to_graph[time]:
                time_to_graph[time][y] = []
            time_to_graph[time][y].append(x)

        def dfs(node: int, graph: Dict[int, List[int]]):
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr, graph)

        time_seq = list(time_to_graph.keys())
        time_seq.sort()
        for time in time_seq:
            experts_in_meeting = time_to_graph[time]
            for e1 in experts_in_meeting.keys():
                if e1 in visited:
                    dfs(e1, experts_in_meeting)
        return list(visited)


# class Solution:
#     def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
#         M = len(meetings)
#         known = set()
#         known.add(0)
#         known.add(firstPerson)
#         visited = set()
#
#         def dfs(node: int):
#             visited.add(node)
#             known.add(node)
#             for sub in g[node]:
#                 if sub not in visited:
#                     dfs(sub)
#
#         meetings.sort(key=lambda m: m[2])
#         i = 0
#         while i < M:
#             visited = set()
#             time = meetings[i][-1]
#             g = defaultdict(list)
#             while i < M and meetings[i][-1] == time:
#                 u, v, _ = meetings[i]
#                 g[u].append(v)
#                 g[v].append(u)
#                 i += 1
#             for j in g.keys():
#                 if j in known:
#                     dfs(j)
#
#         return list(known)


# class Solution:
#     def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
#         known_state = [False] * n
#         known_state[0] = True
#         known_state[firstPerson] = True
#         g = [[] for _ in range(n)]
#         for u, v, t in meetings:
#             g[u].append((v, t))
#             g[v].append((u, t))
#
#         visited = set()
#
#         def dfs(node: int, time: int):
#             visited.add(node)
#             known_state[node] = True
#             for sub, t in g[node]:
#                 if sub not in visited and t >= time:
#                     dfs(sub, time)
#
#         meetings.sort(key=lambda m: m[2])
#         for u, v, t in meetings:
#             visited.clear()
#             if known_state[u]:
#                 known_state[v] = True
#             if known_state[v]:
#                 known_state[u] = True
#             if known_state[u]:
#                 dfs(u, t)
#
#         return [i for i in range(n) if known_state[i]]


def check(n: int, meetings: List[List[int]], firstPerson: int, expect: List[int]):
    output = Solution().findAllPeople(n, meetings, firstPerson)
    utils.tst(f'n={n} meetings={meetings} firstPerson={firstPerson}', output, expect)


if __name__ == '__main__':
    # check(12,
    #       [[10, 8, 6], [9, 5, 11], [0, 5, 18], [4, 5, 13], [11, 6, 17], [0, 11, 10], [10, 11, 7], [5, 8, 3], [7, 6, 16],
    #        [3, 6, 10], [3, 11, 1], [8, 3, 2], [5, 0, 7], [3, 8, 20], [11, 0, 20], [8, 3, 4], [1, 9, 4], [10, 7, 11],
    #        [8, 10, 18]], 9, [0, 1, 4, 5, 6, 9, 11])
    check(6, [[0, 2, 1], [1, 3, 1], [4, 5, 1]], 1, [0, 1, 2, 3])
