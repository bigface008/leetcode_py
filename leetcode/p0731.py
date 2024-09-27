# https://leetcode.com/problems/my-calendar-ii/?envType=daily-question&envId=2024-09-27
from collections import defaultdict
from typing import List, Optional


class Node:
    def __init__(self):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.val = 0
        self.add = 0


def pushdown(node: Node):
    if not node.left:
        node.left = Node()
    if not node.right:
        node.right = Node()
    if node.add == 0:
        return
    node.left.val += node.add
    node.right.val += node.add
    node.left.add += node.add
    node.right.add += node.add
    node.add = 0


def pushup(node: Node):
    node.val = max(node.right.val, node.left.val)


def query(node: Node, start: int, end: int, l: int, r: int) -> int:
    if l <= start and end <= r:
        return node.val
    pushdown(node)
    mid = (start + end) // 2
    ans = 0
    if l <= mid:
        ans = query(node.left, start, mid, l, r)
    if r > mid:
        ans = max(ans, query(node.right, mid + 1, end, l, r))
    return ans


def update(node: Node, start: int, end: int, l: int, r: int, val: int):
    if l <= start and end <= r:
        node.val += val
        node.add += val
        return
    pushdown(node)
    mid = (start + end) // 2
    if l <= mid:
        update(node.left, start, mid, l, r, val)
    if r > mid:
        update(node.right, mid + 1, end, l, r, val)
    pushup(node)


class MyCalendarTwo:

    def __init__(self):
        # self.diff = []
        # self.diff = defaultdict(int)
        self.root = Node()
        self.N = pow(10, 9)

    def book(self, start: int, end: int) -> bool:
        if query(self.root, 0, self.N, start, end - 1) >= 2:
            return False
        update(self.root, 0, self.N, start, end - 1, 1)
        return True


if __name__ == '__main__':
    d = {}
    d['b'] = 'b'
    d['a'] = 'a'
    d['c'] = 'c'
    print(list(d.keys()))
    print(sorted(list(d.keys())))
