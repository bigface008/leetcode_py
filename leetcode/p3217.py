from typing import List, Optional
from utils import ListNode


# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2024-09-06
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        st = set(nums)
        extra = ListNode(0)
        extra.next = head
        prev = extra
        curr = head
        while curr is not None:
            if curr.val in st:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return extra.next