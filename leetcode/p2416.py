from collections import defaultdict, Counter
from typing import List, Optional


# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/?envType=daily-question&envId=2024-09-25
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        N = len(words)
        ans = [0] * N
        root = TrieNode('#')
        for wd in words:
            root.add(wd)

        for i, wd in enumerate(words):
            ans[i] = root.search(wd)
        return ans


        # N = len(words)
        # ans = [0] * N
        # seen = Counter()
        # for wd in words:
        #     for i in range(len(wd)):
        #         seen[wd[:i + 1]] += 1
        #
        # for i, wd in enumerate(words):
        #     tmp = 0
        #     for j in range(len(wd)):
        #         sub_wd = wd[:j + 1]
        #         if sub_wd not in seen:
        #             break
        #         tmp += seen[sub_wd]
        #     ans[i] = tmp
        # return ans


class TrieNode:
    def __init__(self, ch: str):
        self.ch = ch
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.count = 0

    def add(self, word: str):
        p = self
        for i, ch in enumerate(word):
            x = ord(ch) - ord('a')
            if p.children[x] is None:
                p.children[x] = TrieNode(ch)
            p = p.children[x]
            p.count += 1

    def search(self, word: str) -> int:
        p = self
        ans = 0
        for ch in word:
            x = ord(ch) - ord('a')
            if p.children[x] is None:
                return ans
            p = p.children[x]
            ans += p.count
        return ans
