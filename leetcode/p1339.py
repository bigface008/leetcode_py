# https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/?envType=daily-question&envId=2026-01-07
from collections import defaultdict

from utils import TreeNode
from typing import Optional, Dict, Tuple, List


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = pow(10, 9) + 7
        sub_sum: List[int] = []
        total = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            nonlocal total
            total += node.val
            res = node.val + dfs(node.left) + dfs(node.right)
            sub_sum.append(res)
            return res

        dfs(root)
        return max(x * (total - x) for x in sub_sum) % MOD



        # MOD = pow(10, 9) + 7
        # seq_to_node: Dict[int, Tuple[TreeNode, int]] = dict()
        # seq_to_subtree_sum: Dict[int, int] = dict()
        # seq_to_subnode_seq: Dict[int, List[Optional[int]]] = defaultdict(list)
        #
        # seq = 0
        # def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[int]]:
        #     if node is None:
        #         return 0, None
        #     nonlocal seq
        #     curr_idx = seq
        #     seq += 1
        #     left_sum, left_idx = dfs(node.left)
        #     right_sum, right_idx = dfs(node.right)
        #     seq_to_subnode_seq[curr_idx] = [left_idx, right_idx]
        #     res = left_sum + right_sum + node.val
        #     seq_to_subtree_sum[curr_idx] = res
        #     return res, curr_idx
        #
        # ans = 0
        #
        # def dfs2(node: Optional[TreeNode], parent_sum: int):
        #     if node is None:
        #         return
        #     nonlocal seq
        #     curr_idx = seq
        #     seq += 1
        #     left_idx, right_idx = seq_to_subnode_seq[curr_idx]
        #     left_sum = seq_to_subtree_sum[left_idx] if left_idx is not None else 0
        #     right_sum = seq_to_subtree_sum[right_idx] if right_idx is not None else 0
        #     r1 = left_sum * (right_sum + parent_sum + node.val)
        #     r2 = right_sum * (left_sum + parent_sum + node.val)
        #     nonlocal ans
        #     ans = max(ans, r1, r2)
        #     dfs2(node.left, right_sum + parent_sum + node.val)
        #     dfs2(node.right, left_sum + parent_sum + node.val)
        #
        # dfs(root)
        # seq = 0
        # dfs2(root, 0)
        # return ans % MOD


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    # print(Solution().m
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(6)
    print(Solution().maxProduct(root))