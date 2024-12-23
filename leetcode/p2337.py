# https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/?envType=daily-question&envId=2024-12-05
import utils


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        a1 = []
        for i, ch in enumerate(start):
            if ch != '_':
                a1.append((ch, i))
        a2 = []
        for i, ch in enumerate(target):
            if ch != '_':
                a2.append((ch, i))
        if len(a1) != len(a2):
            return False
        for (ch1, i1), (ch2, i2) in zip(a1, a2):
            if ch1 != ch2:
                return False
            if ch1 == 'L' and i1 < i2:
                return False
            if ch1 == 'R' and i2 < i1:
                return False
        return True


# class Solution:
#     def canChange(self, start: str, target: str) -> bool:
#         N = len(start)
#         i2 = 0
#         cnt1 = 0; cnt2 = 0
#         for i1, ch1 in enumerate(start):
#             if ch1 == '_':
#                 continue
#             cnt1 += 1
#             while i2 < N and target[i2] == '_':
#                 i2 += 1
#             cnt2 += 1
#             if i2 == N:
#                 return False
#             ch2 = target[i2]
#             if ch1 != ch2:
#                 return False
#             if ch1 == 'L' and i1 < i2:
#                 return False
#             if ch1 == 'R' and i2 < i1:
#                 return False
#             match1 = i1
#             i2 += 1
#         return cnt1 == cnt2


        # i2 = 0
        # for i1, ch1 in enumerate(start):
        #     if ch1 == '_':
        #         continue
        #     while i2 < N and target[i2] == '_':
        #         i2 += 1
        #     if i2 == N:
        #         return False
        #     ch2 = target[i2]
        #     if ch1 != ch2:
        #         return False
        #     i2 += 1
        # return True


def check(start: str, target: str, expect: bool):
    output = Solution().canChange(start, target)
    utils.tst(f'start={start} target={target}', output, expect)


if __name__ == '__main__':
    # check('_L__R__R_', 'L______RR', True)
    # check('_R', 'R_', True)
