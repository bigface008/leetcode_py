# 对一个01组成的字符串，选定第i个数，将[0,i]内的数反转，这样成为一次操作
# 对一个01串，最少执行k次操作可以将其全部变成1，则把k成为其权重
# 对一个01串，求其所有的长度为奇数的连续子串中，权重为奇数的个数
import math

import utils


def sol2(ss: str) -> int:
    N = len(ss)
    arr = [int(s) for s in ss]
    ans = 0
    for i in range(N):
        wt = 1 - arr[i]
        if wt == 1:
            # ans += len(range(i + 1, N + 1, 2))
            ans += math.ceil((N - i) / 2)
    return ans


def sol1(ss: str) -> int:
    N = len(ss)
    arr = [int(s) for s in ss]
    ans = 0
    for i in range(N):
        window_cnt = 1 - arr[i]
        if window_cnt % 2 == 1:
            ans += 1
        for j in range(i + 1, N + 1, 2):
            group = arr[j - 3:j]
            if group == [0, 0, 0]:
                pass
            elif group == [0, 1, 0]:
                window_cnt += 2
            elif group == [0, 0, 1]:
                pass
            elif group == [0, 1, 1]:
                pass
            elif group == [1, 1, 1]:
                pass
            elif group == [1, 0, 0]:
                window_cnt += 2
            elif group == [1, 1, 0]:
                window_cnt += 2
            elif group == [1, 0, 1]:
                window_cnt += 2
            if window_cnt % 2 == 1:
                ans += 1
    return ans



def tst(ss: str, expect: int):
    output = sol1(ss)
    utils.tst(f'test ss={ss}', output, expect)


if __name__ == '__main__':
    tst('01010', 5)