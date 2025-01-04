# https://leetcode.cn/problems/find-eventual-safe-states/
from typing import List
from functools import cache

import utils


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        states = [0] * N

        def isSafe(node: int) -> bool:
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True

            states[node] = 1
            for sub in graph[node]:
                if not isSafe(sub):
                    return False
            states[node] = 2
            return True

        return [i for i in range(N) if isSafe(i)]


def check(graph: List[List[int]], expect: List[int]):
    output = Solution().eventualSafeNodes(graph)
    utils.tst(f'graph={graph}', output, expect)


if __name__ == '__main__':
    check([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6])
