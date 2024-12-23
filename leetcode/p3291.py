# https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/?envType=daily-question&envId=2024-12-17
from collections import defaultdict
from typing import List, Optional
from functools import cache
from math import inf


class Node:
    def __init__(self):
        self.children = {} # char -> Node
        self.is_word = False


class TrieTree:
    def __init__(self):
        self.root = Node()

    def add(self, word: str):
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_word = True

    def find(self, word: str) -> bool:
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def find2(self, target: str, pos: int) -> List[int]:
        node = self.root
        ans = []
        for i in range(pos, len(target)):
            ch = target[i]
            if ch not in node.children:
                break
            node = node.children[ch]
            ans.append(i - pos + 1)
        return ans


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        N = len(target)
        tree = TrieTree()
        for word in words:
            tree.add(word)

        dp = [inf] * (N + 1)
        dp[0] = 0
        for i in range(N):
            if dp[i] is inf:
                continue
            indices = tree.find2(target, i)
            for l in indices:
                dp[i + l] = min(dp[i + l], dp[i] + 1)
        return dp[-1] if dp[-1] is not inf else -1


class Solution2:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tree = TrieTree()
        for word in words:
            tree.add(word)

        @cache
        def dfs(word: str) -> int:
            if not word:
                return 0
            node = tree.root
            stop_i = -1
            ans = inf
            for i, ch in enumerate(word):
                if ch not in node.children:
                    stop_i = i - 1
                    break
                ans = min(ans, 1 + dfs(word[i + 1:]))
                node = node.children[ch]
            # if stop_i == -1:
            #     return inf # TODO
            return ans

        res = dfs(target)
        return res if res is not inf else -1


if __name__ == '__main__':
    word = 'abc'
    print(word[3:] == '')
    print(word[2:])