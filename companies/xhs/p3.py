import sys
from collections import defaultdict
from typing import List, Dict

# TODO: 问题的重点在于，对一个图（树）如何快速遍历出每两个节点之间的边的权值？
# TODO: xor的特殊属性！这里的权值是各个连续边的xor值！而xor是可以前缀和的！

N, Q = [int(s) for s in sys.stdin.readline().split()]
graph = defaultdict(dict)
edges = []
visited = [False] * N
infoMp = defaultdict(dict) # xor -> u -> vs

def store(u: int, v: int, w: int):
    if u not in infoMp[w]:
        infoMp[w][u] = set()
    infoMp[w][u].add(v)
    if v not in infoMp[w]:
        infoMp[w][v] = set()
    infoMp[w][v].add(u)

for _ in range(N - 1):
    u, v, w = [int(s) for s in sys.stdin.readline().split()]
    graph[u][v] = w
    graph[v][u] = w
    edges.append((u, v, w))
    store(u, v, w)

path = []

def dfs(start: int, curr: int, xorVal: int):
    allVisited = True
    for nbr, wt in graph[curr]:
        if not visited[nbr]:
            path.append((curr, nbr, wt))
            visited[nbr] = True
            dfs(start, nbr, xorVal ^ wt)
            allVisited = False
            path.pop()
    if allVisited:
        for i in enumerate(path):
            start, _, wt = path[i]
            acc_wt = 0
            for j in range(i + 1, len(path)):
                wt = path[j - 1][2]
                acc_wt ^= wt
                store(start, path[j][1], acc_wt)


def sol(u: int, k: int) -> int:
    xor = u ^ k
    if xor not in infoMp:
        return 0
    mp = infoMp[xor]
    if u not in mp:
        return 0
    return len(mp[u])


# dfs(1, 1, 0)
# for _ in range(Q):
#     u, k = [int(s) for s in sys.stdin.readline().split()]
#     print(sol(u, k))


# 利用了xor特性
def sol2() -> int:
    # 首先任选一个起点，利用dfs/bfs计算出它到所有其他节点的距离
    pre_xor = [0] * (N + 1)
    visited = [False] * N
    visited[0] = True
    dfs1(1, 0, pre_xor, visited)

    # 接着，对于任意query中的u，v，xor[u, v] = pre_xor[u, start] ^ pre_xor[v, start]
    # for q in ...



def dfs1(curr: int, xor: int, pre_xor: List[int], visited: List[int]):
    pre_xor[curr] = xor
    for nbr, wt in graph[curr].items():
        if not visited[nbr - 1]:
            visited[nbr - 1] = True
            dfs1(nbr, xor ^ wt, pre_xor, visited)


if __name__ == '__main__':
    print('Hello')