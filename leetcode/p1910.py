# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/?envType=daily-question&envId=2025-02-11
import utils


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        idx = s.find(part)
        while idx != -1:
            s = s[:idx] + s[idx + len(part):]
            idx = s.find(part)
        return s


def check(s: str, part: str, expect: str):
    output = Solution().removeOccurrences(s, part)
    utils.tst(f's={s} part={part}', output, expect)


if __name__ == '__main__':
    check('daabcbaabcbc', 'abc', 'dab')
