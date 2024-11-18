import collections
import heapq
from typing import Optional
from utils import TreeNode


# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/?envType=daily-question&envId=2024-10-22
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        dq = collections.deque()
        dq.append(root)
        pq = []
        level_cnt = 0
        while dq:
            size = len(dq)
            level_sum = 0
            level_cnt += 1
            for _ in range(size):
                node = dq.popleft()
                level_sum += node.val
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            if len(pq) < k:
                heapq.heappush(pq, level_sum)
            elif pq[0] < level_sum:
                heapq.heappop(pq)
                heapq.heappush(pq, level_sum)
        if level_cnt < k:
            return -1
        return pq[0]