# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/?envType=daily-question&envId=2026-01-09
from collections import deque
from typing import Optional, Set
from utils import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = -1
        ans: Optional[TreeNode] = None

        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal max_depth
            nonlocal ans
            if node is None:
                max_depth = max(max_depth, depth)
                return depth
            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)
            if left_depth == right_depth == max_depth:
                ans = node
            return max(left_depth, right_depth)

        dfs(root, 0)
        return ans

        # dq = deque()
        # dq.append(root)
        # level_set = set()
        # while dq:
        #     level_size = len(dq)
        #     level_set = set(dq)
        #     for _ in range(level_size):
        #         node = dq.popleft()
        #         if node.left:
        #             dq.append(node.left)
        #         if node.right:
        #             dq.append(node.right)
        #
        # stack = deque()
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     if node is None:
        #
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        #
        # def dfs(node: Optional[TreeNode]) -> Set[TreeNode]:
        #     subtree_set = set()
        #     if node is None:
        #         return subtree_set
        #     subtree_set.add(node)
        #     subtree_set = subtree_set.union(dfs(node.left))
        #     subtree_set = subtree_set.union(dfs(node.right))
        #     if subtree_set.issuperset(level_set):
        #
        #     return subtree_set

