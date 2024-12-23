# https://leetcode.cn/problems/sort-the-students-by-their-kth-score/description/?envType=daily-question&envId=2024-12-21
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda r: r[k], reverse=True)