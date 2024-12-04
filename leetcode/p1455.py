# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/?envType=daily-question&envId=2024-12-02
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        K = len(searchWord)
        for i, wd in enumerate(sentence.split()):
            if len(wd) >= K and wd[:K] == searchWord:
                return i + 1
        return -1
