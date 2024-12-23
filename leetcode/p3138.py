# https://leetcode.cn/problems/minimum-length-of-anagram-concatenation/description/?envType=daily-question&envId=2024-12-20
import utils
from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        N = len(s)
        cnt = Counter()
        for k in range(1, N // 2 + 1):
            cnt[s[k - 1]] += 1
            if N % k != 0:
                continue
            valid = True
            for i in range(k * 2, N + 1, k):
                if cnt != Counter(s[i - k:i]):
                    valid = False
                    break
            if valid:
                return k
        return N


        # N = len(s)
        # l = 1
        # cnt = Counter()
        # while l <= N:
        #     if N % l != 0:
        #         cnt[s[l - 1]] += 1
        #         l += 1
        #         continue
        #     valid = True
        #     div = N // l
        #     cnt[s[l - 1]] += 1
        #     for i in range(1, div):
        #         cnt2 = Counter(s[i * l:(i + 1) * l])
        #         if len(cnt) != len(cnt2):
        #             valid = False
        #             break
        #         for k, v in cnt.items():
        #             if cnt2[k] != v:
        #                 valid = False
        #                 break
        #         if not valid:
        #             break
        #     if valid:
        #         return l
        #     l += 1
        # return N


def check(s: str, expect: int):
    output = Solution().minAnagramLength(s)
    utils.tst(f'{s}', output, expect)


if __name__ == '__main__':
    # check('abab', 2)
    # check('abba', 2)
    check('aabbabab', 4)