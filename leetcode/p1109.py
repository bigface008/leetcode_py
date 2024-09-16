from itertools import accumulate
from typing import List


# https://leetcode.cn/problems/corporate-flight-bookings/
# To solve this problem, we can use a difference array. We have \( N \) planes,
# and initially, each plane has 0 tickets, which can be represented as an array
# of length \( N \) initialized to 0. For each booking record, we need to add
# the number of seats to all planes in the specified range. Using the difference
# array technique, we can simply update the first element of the range by adding
# the seats and the element right after the last plane in the range by
# subtracting the seats.
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats
        ans = list(accumulate(diff)[:-1])
        return ans
