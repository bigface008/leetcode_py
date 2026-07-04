# https://leetcode.com/problems/grumpy-bookstore-owner/
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        satisfied_cnt = 0
        for i in range(minutes):
            if i < N:
                satisfied_cnt += customers[i]
        for i in range(minutes, N):
            if grumpy[i] == 0:
                satisfied_cnt += customers[i]
        ans = satisfied_cnt
        for i in range(minutes, N):
            if grumpy[i] == 1:
                satisfied_cnt += customers[i]
            if grumpy[i - minutes] == 1:
                satisfied_cnt -= customers[i - minutes]
            ans = max(ans, satisfied_cnt)
        return ans