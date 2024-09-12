from typing import Optional, List
from utils import ListNode


# https://leetcode.com/problems/split-linked-list-in-parts/?envType=daily-question&envId=2024-09-08
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1

        group_len = cnt // k
        remain = cnt - group_len * k
        each_cnt = [group_len] * k
        for i in range(remain):
            each_cnt[i] += 1

        curr = head
        ans = [None] * k
        for i, ec in enumerate(each_cnt):
            ans[i] = curr
            for j in range(ec):
                if j == ec - 1:
                    tmp = curr.next
                    curr.next = None
                    curr = tmp
                else:
                    curr = curr.next
        return ans