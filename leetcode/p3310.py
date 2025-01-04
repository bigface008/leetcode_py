# https://leetcode.cn/problems/remove-methods-from-project/description/
from typing import List
from functools import cache

import utils


# class Solution:
#     def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
#         g = [[] for _ in range(n)]
#         rg = [[] for _ in range(n)]
#         for u, v in invocations:
#             g[u].append(v)
#             rg[v].append(u)
#         suspect = [False] * n
#         visited = [False] * n
#
#         def dfs(node: int):
#             visited[node] = True
#             suspect[node] = True
#             for nxt in g[node]:
#                 if not visited[nxt]:
#                     dfs(nxt)
#
#         def isRemovable(node: int) -> bool:
#             visited[node] = True
#             for pa in rg[node]:
#                 if not suspect[pa]:
#                     return False
#             for nxt in g[node]:
#                 if not visited[nxt]:
#                     if not isRemovable(nxt):
#                         return False
#             return True
#
#         dfs(k)
#         visited = [False] * n
#         if isRemovable(k):
#             return [i for i in range(n) if not suspect[i]]
#         else:
#             return list(range(n))


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
            rg[v].append(u)
        suspicious = set()

        def dfs(node: int):
            suspicious.add(node)
            for nxt in g[node]:
                if nxt not in suspicious:
                    dfs(nxt)

        dfs(k)
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]


def check(n: int, k: int, invocations: List[List[int]], expect: List[int]):
    output = Solution().remainingMethods(n, k, invocations)
    utils.tst(f'n={n} k={k} invocations={invocations}', output, expect)


if __name__ == '__main__':
    check(3, 2, [[1, 0], [2, 0]], [0, 1, 2])
