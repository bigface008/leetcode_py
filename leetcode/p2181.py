from typing import Optional
from utils import ListNode


# https://leetcode.cn/problems/merge-nodes-in-between-zeros/description/?envType=daily-question&envId=2024-09-09
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        extra = ListNode(0)
        extra.next = head
        prev_zero = extra # not zero, but the node before zero
        curr = head.next
        v_sum = 0
        while curr is not None:
            if curr.val == 0:
                prev_zero.next = ListNode(v_sum)
                prev_zero.next.next = curr.next
                prev_zero = prev_zero.next
                v_sum = 0
            else:
                v_sum += curr.val
            curr = curr.next
        return extra.next
