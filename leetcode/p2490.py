# https://leetcode.com/problems/circular-sentence/?envType=daily-question&envId=2024-11-02
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        N = len(sentence)
        if sentence[0] != sentence[-1]:
            return False
        for i, ch in enumerate(sentence):
            if ch == ' ' and sentence[i + 1] != sentence[i - 1]:
                return False
        return True

