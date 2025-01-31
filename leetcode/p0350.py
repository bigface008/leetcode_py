# https://leetcode.cn/problems/intersection-of-two-arrays-ii/?envType=daily-question&envId=2025-01-30
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for k1, v1 in cnt1.items():
            if k1 not in cnt2:
                continue
            v2 = cnt2[k1]
            for _ in range(min(v1, v2)):
                ans.append(k1)
        return ans