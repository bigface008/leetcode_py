# https://leetcode.cn/problems/reduce-array-size-to-the-half/?envType=daily-question&envId=2024-12-15
from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        cnt = Counter(arr)
        info = [(v, k) for k, v in cnt.items()]
        info.sort(reverse=True)
        freq_sum = 0
        for i, (freq, num) in enumerate(info):
            freq_sum += freq
            if freq_sum >= N // 2:
                return i + 1
        return -1