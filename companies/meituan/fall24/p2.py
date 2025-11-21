import sys
from typing import List
from functools import cache


def solution(N: int, K: int, X: int, arr: List[int]) -> int:
    seen = set()
    mex = [0] * N
    mex_val = 0
    for i in range(N - 1, -1, -1):
        x = arr[i]
        seen.add(x)
        while mex_val in seen:
            mex_val += 1
        mex[i] = mex_val

    dp = [0] * (N + 1)
    for i in range(N, -1, -1):
        if i == N:
            dp[i] = 0
            continue
        plan1 = X + dp[i + 1]
        plan2 = K * mex[i]
        dp[i] = min(plan1, plan2)

    return dp[0]


T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, K, X = list([int(s) for s in sys.stdin.readline().strip().split()])
    arr = list([int(s) for s in sys.stdin.readline().strip().split()])
    print(solution(N, K, X, arr))
