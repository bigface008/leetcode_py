# https://leetcode.cn/problems/find-indices-of-stable-mountains/description/?envType=daily-question&envId=2024-12-19
from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]
