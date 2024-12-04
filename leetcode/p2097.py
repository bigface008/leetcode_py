from collections import defaultdict, deque
from itertools import pairwise
from typing import List

from twisted.web.html import output

import utils


# https://leetcode.com/problems/valid-arrangement-of-pairs/?envType=daily-question&envId=2024-11-30
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        nodes = set()
        graph = defaultdict(set)
        in_degrees = defaultdict(int)
        out_degrees = defaultdict(int)
        for start, end in pairs:
            nodes.add(start)
            nodes.add(end)
            graph[start].add(end)
            in_degrees[end] += 1
            out_degrees[start] += 1

        start = -1
        for node in nodes:
            if out_degrees[node] - in_degrees[node] == 1:
                start = node
                break
        if start == -1:
            start = next((n for n in nodes), None)
        if start is None:
            return []

        stk = [node]
        path = deque()
        while stk:
            node = stk[-1]
            if graph[node]:
                next_node = graph[node].pop()
                stk.append(next_node)
            else:
                path.append(stk.pop())

        ans = []
        for p in pairwise(reversed(path)):
            ans.append(p)
        return ans


class Solution2:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        N = len(pairs)
        in_degrees = [0] * N
        graph = [[] for _ in range(N)]
        rgraph = [[] for _ in range(N)]
        start_to_pair_idx = defaultdict(set)
        for i, (start, end) in enumerate(pairs):
            start_to_pair_idx[start].add(i)
        for i, (start, end) in enumerate(pairs):
            for neighbor in start_to_pair_idx[end]:
                graph[i].append(neighbor)
                rgraph[neighbor].append(i)
                in_degrees[neighbor] += 1

        dq = deque()
        for i, d in enumerate(in_degrees):
            if d == 0:
                dq.append(i)
        ans = []

        while dq:
            idx = dq.popleft()
            ans.append(pairs[idx])
            for neighbor in graph[idx]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    dq.append(neighbor)

        if len(ans) == N:
            return ans
        next_start = -1
        for i, d in enumerate(in_degrees):
            if d == 0:
                continue
            # in cycle
            if len(rgraph[i]) == 1 and not ans:
                next_start = i
                break
            if len(rgraph[i]) == 2:
                next_start = i
                break
        if next_start == -1:
            return ans  # TODO:???

        in_degrees[next_start] = 0
        dq.append(next_start)
        while dq:
            idx = dq.popleft()
            ans.append(pairs[idx])
            for neighbor in graph[idx]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    dq.append(neighbor)
        return ans


def tst(pairs: List[List[int]], expect: List[List[int]]):
    output = Solution().validArrangement(pairs)
    utils.tst(f'valid arrangement of pairs={pairs}', output, expect)


if __name__ == '__main__':
    tst([[1, 3], [3, 2], [2, 1]], [[1, 3], [3, 2], [2, 1]])
