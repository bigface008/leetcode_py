from typing import Optional, List
from utils import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        extra = ListNode()
        extra.next = head
        curr = head
        prev = extra
        while curr and curr.next:
            n1 = curr
            n2 = curr.next
            curr = n2.next
            n2.next = n1
            n1.next = curr
            prev.next = n2
            prev = n1
        return extra.next
