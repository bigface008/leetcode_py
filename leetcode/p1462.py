# https://leetcode.com/problems/course-schedule-iv/?envType=daily-question&envId=2025-01-27
import collections
from typing import List, Set


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        post_set = [set() for _ in range(numCourses)]

        def dfs(node: int) -> Set[int]:
            for sub in graph[node]:
                if sub not in post_set[node]:
                    post_set[node].add(sub)
                    post_set[node].update(dfs(sub))
            return post_set[node]

        for i in range(numCourses):
            dfs(i)

        return [(b in post_set[a]) for a, b in queries]


class Solution3:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        f = [[False] * numCourses for _ in range(numCourses)]
        g = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for a, b in prerequisites:
            in_degrees[b] += 1
            g[a].append(b)

        dq = collections.deque(i for i in range(numCourses) if in_degrees[i] == 0)
        while dq:
            x = dq.popleft()
            for y in g[x]:
                f[x][y] = True
                for z in range(numCourses):
                    f[z][y] = f[z][y] or f[z][x]
                in_degrees[y] -= 1
                if in_degrees[y] == 0:
                    dq.append(y)
        return [f[a][b] for a, b in queries]

class Solution2:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        # graph = [[] for _ in range(numCourses)]
        rgraph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            # graph[a].append(b)
            rgraph[b].append(a)

        visited = [False] * numCourses

        def dfs(node: int, dep: int) -> bool:
            if visited[node]:
                return False
            visited[node] = True
            if node == dep:
                return True
            for prev in rgraph[node]:
                if not visited[prev] and dfs(prev, dep):
                    return True
            return False

        ans = [False] * len(queries)
        for i, (a, b) in enumerate(queries):
            ans[i] = dfs(b, a)
            visited = [False] * numCourses
        return ans