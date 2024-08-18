from collections import defaultdict

import utils


# https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        N = len(word)
        if N % k != 0:
            return -1
        kWords = defaultdict(int)
        for i in range(0, N, k):
            kWords[word[i:i + k]] += 1
        return int(N / k - max(kWords.values()))


def tst(word: str, k: int, expect: int):
    output = Solution().minimumOperationsToMakeKPeriodic(word, k)
    utils.tst(f'min operations word={word} k={k}', output, expect)


if __name__ == '__main__':
    tst("leetcodeleet", 4, 1)