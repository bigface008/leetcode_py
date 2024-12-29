# https://leetcode.com/problems/find-largest-value-in-each-tree-row/?envType=daily-question&envId=2024-12-25
from collections import deque
from typing import Optional, List
from utils import TreeNode
from math import inf


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        dq = deque()
        dq.append(root)
        ans = []
        while dq:
            level_size = len(dq)
            res = -inf
            for _ in range(level_size):
                node = dq.popleft()
                res = max(res, node.val)
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            ans.append(res)
        return ans