# https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07
import bisect
from typing import List

import utils


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, word in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j or len(word) > len(word2):
                    continue
                if word2.find(word) != -1:
                    ans.append(word)
                    break
        return ans


class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:
        N = len(words)
        ans = []
        words.sort(key=lambda w: len(w))
        for wi, word in enumerate(words):
            # pos = bisect.bisect_left(range(0, N), True, key=lambda w: len(w) >= len(word))
            found = False
            for i in range(N - 1, -1, -1):
                if i == wi:
                    break
                wd = words[i]
                if len(word) > len(wd) or (len(word) == len(wd) and word != wd):
                    break
                pos = 0
                while pos + len(word) <= len(wd):
                    if wd[pos:pos + len(word)] == word:
                        found = True
                        break
                    pos += 1
                if found:
                    break
            if found:
                ans.append(word)
        return ans


def check(words: List[str], expect: List[str]):
    output = Solution().stringMatching(words)
    utils.tst(words, output, expect)


if __name__ == '__main__':
    check(["mass", "as", "hero", "superhero"], ["as", "hero"])
