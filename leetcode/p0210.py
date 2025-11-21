# https://leetcode.cn/problems/course-schedule-ii/
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            in_degrees[a] += 1

        dq = deque(x for x in range(numCourses) if in_degrees[x] == 0)
        ans = []
        while dq:
            node = dq.popleft()
            ans.append(node)
            for sub_node in graph[node]:
                in_degrees[sub_node] -= 1
                if in_degrees[sub_node] == 0:
                    dq.append(sub_node)
        return ans if len(ans) == numCourses else []