import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
ans = sys.stdin.readline().strip()
# passwords = []
len2Pass = defaultdict(set)

for _ in range(N):
    temp = sys.stdin.readline().strip()
    # passwords.append(temp)
    len2Pass[len(temp)].add(temp)
# print(len2Pass)

less_len_cnt = 0
same_len_cnt = 0

for k, v in len2Pass.items():
    if k < len(ans):
        less_len_cnt += len(v)
    elif k == len(ans):
        same_len_cnt = len(v)

min_ans = less_len_cnt + 1
max_ans = less_len_cnt + same_len_cnt
print(min_ans, max_ans)
