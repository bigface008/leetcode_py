from collections import deque
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# https://leetcode.cn/problems/employee-importance/?envType=daily-question&envId=2024-08-26
class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        idToEmp = {}
        for e in employees:
            idToEmp[e.id] = e

        ans = 0
        q = deque() # id
        q.append(id)
        visited = set() # id
        while q:
            eid = q.pop()
            visited.add(eid)
            emp = idToEmp[eid]
            ans += emp.importance
            for sub_eid in emp.subordinates:
                if sub_eid not in visited:
                    q.append(sub_eid)
        return ans
