# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/?envType=daily-question&envId=2026-01-06
from typing import Optional
from utils import TreeNode
from collections import deque
from math import inf


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        ans = 0
        max_level_sum = -inf
        level_idx = 0
        while dq:
            level_idx += 1
            level_size = len(dq)
            level_sum = 0
            for _ in range(level_size):
                node = dq.popleft()
                level_sum += node.val
                if node is None:
                    continue
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            if max_level_sum < level_sum:
                max_level_sum = level_sum
                ans = level_idx
        return ans


if __name__ == '__main__':
    print(Solution().maxLevelSum())