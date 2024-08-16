# 在一个数组中，要求必须交换一对相邻的数字，交换后求最大的相邻两数的乘积
# 一开做题的时候居然没注意到交换的数字必须相邻这一条件......
# 主要思路是，用一个长为3的window遍历整个数组，window中的最大的两个值的乘积就是答案
from typing import List, Tuple, Dict, Set


def solution(arr: List[int]) -> int:
    if len(arr) < 3:
        return arr[0] * arr[1]
    m1, m2 = 0, 0
    for i in range(3):
        num = arr[i]
        if num > m1:
            m2 = m1
            m1 = num
        elif num > m2:
            m2 = num
    ans = m1 * m2
    for i in range(3, len(arr)):
        newWindow = arr[i - 2 : i + 1].copy()
        newWindow.sort()
        ans = max(ans, newWindow[2] * newWindow[1])
    return ans

