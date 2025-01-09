# https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/?envType=daily-question&envId=2025-01-09
from collections import Counter, defaultdict

import utils


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        diff = defaultdict(int)
        for ch in word2:
            diff[ch] += 1

        less = len(diff)
        ans = left = 0
        for ch in word1:
            diff[ch] -= 1
            if diff[ch] == 0:
                less -= 1
            while less == 0:
                if diff[word1[left]] == 0:
                    less += 1
                diff[word1[left]] += 1
                left += 1
            ans += left
        return ans



class Solution2:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt2 = Counter(word2)
        window_cnt = Counter()
        ans = 0
        left = 0
        for right, ch in enumerate(word1):
            window_cnt[ch] += 1
            while True:
                valid = True
                for k, v in cnt2.items():
                    if window_cnt[k] < v:
                        valid = False
                        break
                if not valid:
                    break
                window_cnt[word1[left]] -= 1
                left += 1
            ans += left
        return ans


def check(word1: str, word2: str, expect: int):
    output = Solution().validSubstringCount(word1, word2)
    utils.tst(f'word1={word1} word2={word2}', output, expect)


if __name__ == '__main__':
    check('bcca', 'abc', 1)
