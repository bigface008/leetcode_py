# https://leetcode.com/problems/delete-nodes-and-return-forest/
from collections import Counter
from typing import Optional, List
from utils import TreeNode


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        delete_st = set(to_delete)

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            nr = dfs(node.right)
            nl = dfs(node.left)
            node.right = nr
            node.left = nl
            if node.val not in delete_st:
                return node
            if nr is not None:
                ans.append(nr)
            if nl is not None:
                ans.append(nl)
            return None

        n = dfs(root)
        if n is not None:
            ans.append(n)
        return ans


if __name__ == '__main__':
    cnt = Counter()
    cnt['a'] += 1
    cnt['a'] += 1
    cnt['a'] += 1
    cnt['b'] += 1
    cnt['b'] += 1
    cnt['b'] += 1
    cnt['b'] += 1
    cnt['b'] += 1
    print(min(cnt))
    print(max(cnt))
