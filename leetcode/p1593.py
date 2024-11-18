# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings
import collections


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        N = len(s)

        ans = 0
        def backtrack(idx: int):
            nonlocal ans
            if idx == N:
                ans = max(ans, len(seen))
                return
            for i in range(idx + 1, N + 1):
                sub_s = s[idx:i]
                if sub_s not in seen:
                    seen.add(sub_s)
                    backtrack(i)
                    seen.remove(sub_s)

        backtrack(0)
        return ans

