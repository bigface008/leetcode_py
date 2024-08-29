from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# https://leetcode.com/problems/n-ary-tree-postorder-traversal/?envType=daily-question&envId=2024-08-26
class Solution:
    def postorder(self, root: Node) -> List[int]:
        ans = []

        def dfs(node: Node):
            if not node:
                return
            for c in node.children:
                dfs(c)
            ans.append(node.val)

        dfs(root)
        return ans