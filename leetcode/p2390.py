# https://leetcode.cn/problems/removing-stars-from-a-string/?envType=daily-question&envId=2024-09-14
import utils


class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch == '*':
                if ans:
                    ans.pop()
            else:
                ans.append(ch)
        return ''.join(ans)

        # ls = list(s)
        # i = 0
        # not_star_indices = []
        # while i < len(ls):
        #     ch = ls[i]
        #     if ch == '*':
        #         if not_star_indices:
        #             ls.pop(i)
        #             ls.pop(not_star_indices[-1])
        #             i -= 1
        #             not_star_indices.pop()
        #         else:
        #             ls.pop(i)
        #     else:
        #         not_star_indices.append(i)
        #         i += 1
        # return ''.join(ls)


def tst(s: str, expect: str):
    output = Solution().removeStars(s)
    utils.tst(f'remove stars s={s}', output, expect)


if __name__ == '__main__':
    tst("leet**cod*e", "lecoe")