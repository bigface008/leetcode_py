from typing import List

import utils


# https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2024-09-21
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        s = str(n)
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans


        # ans = []
        # s = str(n)
        # N = len(s)
        #
        # def dfs(size: int, num: int):
        #     if size == N:
        #         return
        #     down = 0 if size != 0 else 1
        #     for i in range(down, 10):
        #         next = num * 10 + i
        #         if next <= n:
        #             ans.append(next)
        #             dfs(size + 1, next)
        #
        # dfs(0, 0)
        # return ans

# 123
# 1 10 100 101 102


        # ans = []
        # s = str(n)
        #
        # def dfs(i: int, num: int, is_limit: bool, is_num: bool):
        #     print(f'i={i}, num={num}, is_limit={is_limit}, is_num={is_num}')
        #     if i == len(s):
        #         print(f'  add num={num}')
        #         ans.append(num)
        #         return
        #     up = int(s[i]) if is_limit else 9
        #     down = 0 if is_num else 1
        #     print(f'  up={up} down={down}')
        #     for d in range(down, up + 1):
        #         dfs(i + 1, num + d * pow(10, len(s) - i - 1), d == up and is_limit, True)
        #     if not is_num:
        #         dfs(i + 1, num, False, False)
        #
        # dfs(0, 0, True, False)
        # return ans


def tst(n: int, expect: List[int]):
    output = Solution().lexicalOrder(n)
    utils.tst(f'lexical order n={n}', output, expect)


def gen(num: int):
    tmp = [str(x) for x in range(1, num + 1)]
    tmp.sort()
    ans = [int(s) for s in tmp]
    print(len(ans))
    print(ans)



if __name__ == '__main__':
    # tst(13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])
    # tst(2, [1, 2])
    gen(123)
    gen(120)
    gen(6294)
    gen(6290)
