# https://leetcode.cn/problems/my-calendar-iii/?envType=daily-question&envId=2025-01-04
from typing import Optional


class Node:
    def __init__(self):
        self.val = 0
        self.add = 0
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class MyCalendarThree:

    def __init__(self):
        self.N = pow(10, 9)
        self.root = Node()

    def book(self, startTime: int, endTime: int) -> int:
        self.update(self.root, 0, self.N, startTime, endTime - 1)
        return self.query(self.root, 0, self.N, 0, self.N)

    def query(self, node: Node, start: int, end: int, l: int, r: int) -> int:
        if l <= start and end <= r:
            return node.val
        mid = (start + end) // 2
        ans = 0
        self.pushDown(node)
        if l <= mid:
            ans = self.query(node.left, start, mid, l, r)
        if mid + 1 <= r:
            ans = max(ans, self.query(node.right, mid + 1, end, l, r))
        return ans

    def update(self, node: Node, start: int, end: int, l: int, r: int):
        if l <= start and end <= r:
            node.val += 1
            node.add += 1
            return
        self.pushDown(node)
        mid = (start + end) // 2
        if l <= mid:
            self.update(node.left, start, mid, l, r)
        if mid + 1 <= r:
            self.update(node.right, mid + 1, end, l, r)
        self.pushUp(node)

    def pushDown(self, node: Node):
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if not node.add:
            return
        node.right.val += node.add
        node.left.val += node.add
        node.right.add += node.add
        node.left.add += node.add
        node.add = 0

    def pushUp(self, node: Node):
        res = 0
        if node.left is not None:
            res = node.left.val
        if node.right is not None:
            res = max(res, node.right.val)
        node.val = res