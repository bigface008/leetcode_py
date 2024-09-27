import collections
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].append(a)

        dq = collections.deque()
        for i, x in enumerate(in_degree):
            if x == 0:
                dq.append(i)

        ans = []
        while dq:
            node = dq.popleft()
            ans.append(node)
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    dq.append(child)
        return len(ans) == numCourses