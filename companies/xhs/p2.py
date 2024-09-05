import sys
from math import inf

# 给定一系列物品按顺序放置，kinds数组表示每个物品的kind是1还是2，movable数组表示物品是否可移动
# 若两个相邻物品类别不同，则不美观度加一，请问最小的不美观度是多少？

N = int(sys.stdin.readline())
kinds = [int(s) for s in sys.stdin.readline().split()]
movable = [int(s) for s in sys.stdin.readline().split()]
# print(f'N={N} kinds)
ans = inf
# m1, m2 = [], set() # movable k1 k2
# for i in range(N):
#     if movable[i]:
#         if kinds[i] == 1:
#             m1.add(i)
#         else:
#             m2.add(i)

# swap 2, 2 and 2, 1
# def sol() -> int:
#     ans = 0
#     diff_k1_d2_st, diff_k1_d1_st = set(), set()
#     diff_k2_d2_st, diff_k2_d1_st = set(), set()
#     all_st = [[set(), set()], [set(), set()]] # (k, d)
#     origin_sum = 0
#     remove_sum = 0
#     for i in range(N):
#         origin_sum += 1 if i >= 1 and kinds[i] != kinds[i - 1] else 0
#         if not movable[i]:
#             continue
#         k = kinds[i]
#         d = calc_diff(i)
#         print(f'i={i} k={k} d={d}')
#         if d == 2 or d == 1:
#             all_st[k - 1][d - 1].add(i)
#         # if c == 2:
#         #     if k == 1:
#         #         diff_k1_d2_st.add(i)
#         #     else:
#         #         diff_k2_d2_st.add(i)
#         #     diff_2_st.add(i)
#         # elif c == 1:
#         #     diff_1_st.add(i)
#     print(f'k1_d1={all_st[0][0]} k1_d2={all_st[0][1]} k2_d1={all_st[1][0]} k2_d2={all_st[1][1]}')
#     print(f'origin_sum={origin_sum}')
#     # 2, 2
#     diff_2_pair_cnt = min(len(all_st[0][1]), len(all_st[1][1]))
#     print(f'diff_2_pair_cnt={diff_2_pair_cnt}')
#     remove_sum += diff_2_pair_cnt * 4
#     # 2, 1
#     remain_2_k1 = len(all_st[0][1]) - diff_2_pair_cnt
#     remain_2_k2 = len(all_st[1][1]) - diff_2_pair_cnt
#     if remain_2_k1 == 0 and remain_2_k2 == 0:
#         pass
#     elif remain_2_k1 == 0: # no remain k1, use k2 d2 and k1 d1
#         diff_2_1_cnt = min(remain_2_k2, len(all_st[0][0]))
#         remove_sum += diff_2_1_cnt * 2
#     else: # no remain k2, use k1 d2 and k2 d1
#         tmp = min(remain_2_k1, len(all_st[1][0]))
#         remove_sum += tmp * 2
#     print(f'remove_sum={remove_sum}')
#     return origin_sum - remove_sum

# def calc_diff(i: int) -> int:
#     diff_cnt = 0
#     if i >= 1 and kinds[i] != kinds[i - 1]:
#         diff_cnt = 1
#     if i < N - 1 and kinds[i + 1] != kinds[i]:
#         diff_cnt += 1
#     return diff_cnt


# def dfs(i: int, ss: int):
#     if i == N:
#         ans = max(ans, ss)
#         return
#     diff_cnt = calc_diff(i)
#     # if i >= 1 and kinds[i] != kinds[i - 1]:
#     #     ss += 1
#     #     diff_cnt = 1
#     # if i < N - 1 and kinds[i + 1] != kinds[i]:
#     #     diff_cnt += 1
#     if not movable[i] or diff_cnt == 0:
#         dfs(i + 1, ss)
#         return
#     dfs(i + 1, ss + (1 if i >= 1 and kinds[i] != kinds[i - 1] else 0))
#     # swap
#     # find
#     for j in range(i + 1, N):
#         if movable[j] and kinds[j] != kinds[i]:
#             kinds[i], kinds[j] = kinds[j], kinds[i]
#             if is_diff:
#                 dfs(i + 1, ss - 1)
#             else:
#     # not swap


# dfs(0, 0)
# print(sol())
print(ans)
