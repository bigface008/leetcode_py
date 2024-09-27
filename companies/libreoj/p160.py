# https://loj.ac/p/160
import sys
from collections import defaultdict
from functools import cache


def solution2() -> int:
    subtree_sizes = [0] * N
    convert = [0] * N
    cnt = -1
    tree = defaultdict(list)

    for i, parent in enumerate(dependencies):
        # if parent != 0:
        tree[parent].append(i + 1)

    def dfs(x: int):
        print(f'dfs x={x}')
        nonlocal cnt
        cnt += 1
        print(f'cnt {cnt}')
        dfn[cnt] = x
        maxn[x] = cnt

        if x not in tree:
            return

        for i, child in enumerate(tree[x]):
            dfs(child)
            maxn[x] = max(maxn[x], maxn[child])


    @cache
    def dfs1(i: int, capacity: int) -> int:
        if i == 0:
            if weights[convert[i]] <= capacity:
                return values[convert[i]]
            else:
                return 0
        if weights[convert[i]] <= capacity:
            return max(dfs1(i - subtree_sizes[i], capacity), dfs1(i, capacity - weights[convert[i]]) + values[convert[i]])
        else:
            return dfs1(i - subtree_sizes[i], capacity)

    return dfs1(N - 1, W)



def solution() -> int:
    dfn = [0] * (N + 1)
    maxn = [0] * (N + 1)
    cnt = -1
    dp = [[0] * (W + 2) for _ in range(N + 2)]
    tree = defaultdict(list)

    for i, parent in enumerate(dependencies):
        # if parent != 0:
        tree[parent].append(i + 1)

    def dfs(x: int):
        print(f'dfs x={x}')
        nonlocal cnt
        cnt += 1
        print(f'cnt {cnt}')
        dfn[cnt] = x
        maxn[x] = cnt

        if x not in tree:
            return

        for i, child in enumerate(tree[x]):
            dfs(child)
            maxn[x] = max(maxn[x], maxn[child])

    dfs(0)
    for i in range(N, -1, -1):
        for j in range(0, W + 1):
            if j >= weights[dfn[i] - 1]:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - weights[dfn[i] - 1]] + values[dfn[i] - 1])
            dp[i][j] = max(dp[i][j], dp[maxn[dfn[i]] + 1][j])

    ans = max(dp[0][:W + 1])
    return ans


if __name__ == '__main__':
    N, W = [int(s) for s in sys.stdin.readline().split()]
    dependencies = [int(s) for s in sys.stdin.readline().split()]
    weights = [int(s) for s in sys.stdin.readline().split()]
    values = [int(s) for s in sys.stdin.readline().split()]
    print(solution())