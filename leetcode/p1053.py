# https://leetcode.com/problems/previous-permutation-with-one-swap/
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)
        i = N - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i >= 0:
            j = N - 1
            while arr[i] <= arr[j]:
                j -= 1
            while j > 0 and arr[j] == arr[j - 1]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        return arr