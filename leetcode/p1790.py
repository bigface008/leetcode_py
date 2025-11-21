# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/?envType=daily-question&envId=2025-02-05
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N = len(s1)
        diff_cnt = 0
        diff_indices = []
        for i in range(N):
            ch1 = s1[i]
            ch2 = s2[i]
            if ch1 == ch2:
                continue
            if diff_cnt == 2:
                return False
            diff_cnt += 1
            diff_indices.append(i)
        if diff_cnt == 0:
            return True
        if diff_cnt == 1:
            return False
        i0, i1 = diff_indices
        return s1[i0] == s2[i1] and s1[i1] == s2[i0]