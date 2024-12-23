# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/?envType=daily-question&envId=2024-12-23
from collections import deque
from typing import Optional, List

import utils
from utils import TreeNode


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        dq = deque()
        dq.append(root)
        ans = 0
        while dq:
            level_size = len(dq)
            arr = [0] * level_size
            for i in range(level_size):
                node = dq.popleft()
                arr[i] = node.val
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            ans += level_size
            temp = sorted(range(level_size), key=lambda i: arr[i])
            visited = [False] * level_size
            for x in temp:
                if visited[x]:
                    continue
                while not visited[x]:
                    visited[x] = True
                    x = temp[x]
                ans -= 1
        return ans


def loopCount(arr: List[int]) -> int:
    N = len(arr)
    temp = sorted(range(N), key=lambda i: arr[i])
    visited = [False] * N
    res = N
    for v in temp:
        if visited[v]:
            continue
        while not visited[v]:
            visited[v] = True
            v = temp[v]
        res -= 1
    return res


def check(arr: List[int], expect: int):
    output = loopCount(arr)
    utils.tst(f'loopCount({arr})', output, expect)


if __name__ == '__main__':
    check([1, 9, 4, 2, 6, 8], 3)
