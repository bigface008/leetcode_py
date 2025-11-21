# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description/?envType=daily-question&envId=2025-11-15
import utils

# if curr == 1:
#   res += curr - right_zero[r]
#   base_one_cnt = curr - right_zero[r]
#   if right_one[right_zero[r]] < curr - sqrt(base_one_cnt):
#      res += sqrt(base_one_cnt)
#   else:
#      res +=


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos0 = [-1]
        total1 = 0
        ans = 0

        for r, ch in enumerate(s):
            if ch == '0':
                pos0.append(r)
            else:
                total1 += 1
                ans += r - pos0[-1]

            for i in range(len(pos0) - 1, 0, -1):
                cnt0 = len(pos0) - i
                if cnt0 * cnt0 > total1:
                    break
                p, q = pos0[i - 1], pos0[i]
                cnt1 = r - q + 1 - cnt0
                ans += max(q - max(cnt0 * cnt0 - cnt1, 0) - p, 0)

        return ans


# def tst(s: str, expect: int):
#     solution = Solution()
#     output = solution.numberOfSubstrings(s)
#     utils.tst(s, output, expect)


if __name__ == '__main__':
    # tst('00011', 5)
    Solution().numberOfSubstrings('011110')