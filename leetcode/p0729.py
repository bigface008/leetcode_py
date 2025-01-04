import bisect
from typing import List, Tuple, Optional

import utils


# https://leetcode.com/problems/my-calendar-i/?envType=daily-question&envId=2024-09-26
class Node:
    def __init__(self):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.val = 0
        self.add = 0


class MyCalendar:

    def __init__(self):
        self.N = pow(10, 9)
        self.root = Node()

    def book(self, start: int, end: int) -> bool:
        if self.query(self.root, 0, self.N, start, end - 1) != 0:
            return False
        self.update(self.root, 0, self.N, start, end - 1)
        return True

    def query(self, node: Node, start: int, end: int, l: int, r: int) -> int:
        if l <= start and end <= r:
            return node.val
        self.pushDown(node)
        mid = (start + end) // 2
        ans = 0
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
        mid = (start + end) // 2
        if l <= mid:
            self.update(node.left, start, mid, l, r)
        if mid + 1 <= r:
            self.update(node.right, mid + 1, end, l, r)
        self.pushUp(node)

    def pushDown(self, node: Node):
        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()
        if node.add == 0:
            return
        node.left.val += node.add
        node.left.add += node.add
        node.right.val += node.add
        node.right.add += node.add
        node.add = 0

    def pushUp(self, node: Node):
        ans = 0
        if node.right:
            ans = node.right.val
        if node.left:
            ans = max(ans, node.left.val)
        node.val = ans


# class Node:
#     def __init__(self):
#         self.left: Optional[Node] = None
#         self.right: Optional[Node] = None
#         self.val = 0
#         self.add = 0
#
#
# def pushdown(node: Node):
#     if node.left is None:
#         node.left = Node()
#     if node.right is None:
#         node.right = Node()
#     if node.add == 0:
#         return
#     node.left.val += node.add
#     node.right.val += node.add
#     node.left.add += node.add
#     node.right.add += node.add
#     node.add = 0
#
#
# def pushup(node: Node):
#     node.val = max(node.left.val, node.right.val)
#
#
# def query(node: Node, start: int, end: int, l: int, r: int) -> int:
#     if l <= start and end <= r:
#         return node.val
#     pushdown(node)
#     mid = (start + end) // 2
#     ans = 0
#     if l <= mid:
#         ans = query(node.left, start, mid, l, r)
#     if r > mid:
#         ans = max(ans, query(node.right, mid + 1, end, l, r))
#     return ans
#
#
# def update(node: Node, start: int, end: int, l: int, r: int, val: int):
#     if l <= start and end <= r:
#         node.val += val
#         node.add += val
#         return
#     pushdown(node)
#     mid = (start + end) // 2
#     if l <= mid:
#         update(node.left, start, mid, l, r, val)
#     if r > mid:
#         update(node.right, mid + 1, end, l, r, val)
#     pushup(node)
#
#
# class MyCalendar:
#
#     def __init__(self):
#         self.root = Node()
#         self.N = pow(10, 9)
#
#     def book(self, start: int, end: int) -> bool:
#         if query(self.root, 0, self.N, start, end - 1) > 0:
#             return False
#         update(self.root, 0, self.N, start, end - 1, 1)
#         return True


class MyCalendar2:

    def __init__(self):
        self.info = []

    def book(self, start: int, end: int) -> bool:
        if not self.info:
            self.info.append(start)
            self.info.append(end)
            return True
        N = len(self.info)
        i1 = bisect.bisect_left(self.info, start)
        if i1 == N:
            self.info.append(start)
            self.info.append(end)
            return True
        if i1 % 2 == 0:
            if self.info[i1] == start:
                return False
            if self.info[i1] < end:
                return False
            if self.info[i1] == end:
                self.info[i1] = start
            else:
                self.info.insert(i1, start)
                self.info.insert(i1 + 1, end)
            return True
        else:
            if self.info[i1] == start:
                if i1 + 1 == N:
                    self.info[i1] = end
                    return True
                elif self.info[i1 + 1] > end:
                    self.info[i1] = end
                    return True
                elif self.info[i1 + 1] == end:
                    self.info.pop(i1 + 1)
                    self.info.pop(i1)
                    return True
                else:
                    return False
            return False


def tst(input: List[List[int]], expect: List[bool]):
    c = MyCalendar()
    output = []
    for s, e in input:
        output.append(c.book(s, e))
    utils.tst(f'input={input}', output, expect)


if __name__ == '__main__':
    n = Node()
    print(n.left)
    # tst([[10, 20], [15, 25], [20, 30]], [True, False, True])
    # tst([[23, 32], [42, 50], [6, 14], [0, 7], [21, 30], [26, 31], [46, 50], [28, 36], [0, 6], [27, 36], [6, 11],
    #      [20, 25], [32, 37], [14, 20], [7, 16], [13, 22], [39, 47], [37, 46], [42, 50], [9, 17], [49, 50], [31, 37],
    #      [43, 49], [2, 10], [3, 12], [8, 14], [14, 21], [42, 47], [43, 49], [36, 43]],
    #     [True, True, True, False, False, False, False, False, True, False, False, False, True, True, False, False,
    #      False, False, False, False, False, False, False, False, False, False, False, False, False, False])
