from typing import Optional
from utils import ListNode


# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/?envType=daily-question&envId=2024-09-10
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        curr = head
        while curr and curr.next:
            new_node = ListNode(gcd(curr.val, curr.next.val))
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        return head
