from typing import List


# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/?envType=daily-question&envId=2024-09-02
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        ss = sum(chalk)
        k %= ss
        for i, cnt in enumerate(chalk):
            if k < cnt:
                return i
            else:
                k -= cnt
        return 0
