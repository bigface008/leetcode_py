# 一棵天赋树，每个节点必须在其父节点解锁的情况下才能解锁（根节点除外）
# 节点i解锁的条件有两种：
# 1. 使用ai个中级材料，1个中级材料可以用X个钻石购买。
# 2. 使用ai个高级材料，1个高级材料可以用Y个钻石购买，或者用1个高级天赋包兑换。
# 每个节点i都有ti、ai、bi三个信息，其中，ti表示解锁条件是1还是2，ai表示材料个数，bi表示节点的力量点数。
# 求给定A个钻石和B个高级天赋包，以及一棵天赋树，求最多能解锁多少力量点数。
from collections import defaultdict
from typing import List

# 一棵天赋树，每个节点必须在其父节点解锁的情况下才能解锁（根节点除外）
# 每个节点i都有ti、ai、bi三个信息，其中，ti表示解锁条件是1还是2，ai表示所需材料个数，bi表示节点的力量点数。
# 1. 当ti为0，使用ai个中级材料，1个中级材料可以用X个钻石购买。
# 2. 当ti为1，使用ai个高级材料，1个高级材料可以用Y个钻石购买，或者用1个高级天赋包兑换。
# 求给定A个钻石和B个高级天赋包，以及一棵天赋树，求最多能解锁多少力量点数。


# 一棵树，每个节点必须在其父节点解锁的情况下才能解锁（根节点除外）
# 每个节点i都有ai、bi两个信息，其中，ai表示所需材料个数，bi表示节点的力量点数。
# 求给定A个材料，求最多能解锁多少力量点数。

def solution2(information: List[int], parents: List[int], A: int):
    tree = defaultdict(list)
    for i, parent in enumerate(parents):
        tree[parent].append(i + 2)

    def dfs1(node: int, remain_a: int) -> int:
        t, a, b = information[node - 1]
        if remain_a < a:
            return 0
        if node not in tree:
            return b

        # TODO: 这个mx是要处理每个子节点的，要怎么处理呢？
        mx = dfs1(0, remain_a - a)
        return mx + b

    return dfs1(1, A)


def solution3(information: List[int], parents: List[int], A: int):
    tree = defaultdict(list)
    for i, parent in enumerate(parents):
        tree[parent].append(i + 2)
    ans = 0
    remain_a = A

    def dfs2(node: int, power_sum: int):
        nonlocal ans
        nonlocal remain_a
        t, a, b = information[node - 1]
        if remain_a < a:
            ans = max(ans, power_sum)
            return
        if node not in tree:
            ans = max(ans, power_sum + b)
            return

        remain_a -= a
        # TODO: 这里是要枚举每个子节点的选与不选的情况并累加的，要怎么处理呢？
        dfs2(0, power_sum + b)
        remain_a += a

    dfs2(1, 0)
    return ans


def solution(informations: List[int], parents: List[int], A: int, B: int, X: int, Y: int):
    tree = defaultdict(list)
    for i, parent in enumerate(parents):
        tree[parent].append(i + 2)
    ans = 0
    remain_A = A
    remain_B = B

    def dfs3(node: int, power_sum: int):
        nonlocal ans
        nonlocal remain_A
        nonlocal remain_B
        ans = max(ans, power_sum + informations[node - 1][2])
        if node not in tree:
            return
        children = tree[node]


    def dfs2(node: int, power_sum: int):
        nonlocal ans
        nonlocal remain_A
        nonlocal remain_B
        ans = max(ans, power_sum)
        if remain_A < 0 or remain_B < 0:
            return
        t, a, b = informations[node - 1]
        if t == 0:
            if remain_A >= X * a:
                remain_A -= X * a
                ans = max(ans, power_sum + b)
                if node in tree:
                    children = tree[node]
                pass # TODO: use A
                remain_A += X * a
            else:
                pass
        else:
            if remain_A >= Y * a:
                pass # use A
            if remain_B >= a:
                pass # use B

    # def dfs(node: int, remain_a: int, remain_b: int) -> int:
    #     if remain_a < 0 or remain_b < 0:
    #         return 0
    #     t, a, b = informations[node - 1]
    #     if node not in tree:
    #         if remain_a >= X * a or remain_a >= Y * a or remain_b >= a:
    #             return b
    #         else:
    #             return 0
    #
    #     if t == 0:
    #         if remain_a >= X * a:
    #             return dfs(0, remain_a - X * a, remain_b) + b
    #         else:
    #             return 0
    #     else:
    #         mx = -b
    #         if remain_a >= Y * a:
    #             mx = max(mx, dfs(0, remain_a - Y * a, remain_b))
    #         if remain_b >= a:
    #             mx = max(mx, dfs(0, remain_a, remain_b - a))
    #         return mx + b
    #
    # return dfs(1, A, B)