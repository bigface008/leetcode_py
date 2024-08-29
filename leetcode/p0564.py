# https://leetcode.com/problems/find-the-closest-palindrome
import heapq


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == '11':
            return '9'

        def pld(num: int) -> int:
            s = list(str(num))
            i, j = 0, len(s) - 1
            while i < j:
                s[j] = s[i]
                # s = s[:j] + s[i] + s[j + 1:]
                i += 1
                j -= 1
            return int(''.join(s))

        ss = int(n)
        ans1, ans2 = ss, ss
        i = 0
        while ans1 >= ss:
            ans1 = pld(ss - pow(10, i))
            i += 1
        i = 0
        while ans2 <= ss:
            ans2 = pld(ss + pow(10, i))
            i += 1
        if ss - ans1 <= ans2 - ss:
            return str(ans1)
        else:
            return str(ans2)


if __name__ == '__main__':
    print(Solution().nearestPalindromic('12345'))
    mh = []
    heapq.heappush(mh, 12)
    heapq.heappush(mh, 2)
    heapq.heappush(mh, -2)
    heapq.heappush(mh, 2)
    print(mh)
    print(mh[-1])
    print(int(12).bit_count())
