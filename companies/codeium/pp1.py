# 第1题是找sorting的key:
# 给1个sorted array of strings，需要找出这个array的sorting key，返回一个array的形式。输出一个正确答案即可
# 例如:输入=["xyz","abc”],答案可以是["zyx...cba"]也可以是["xa"]
from collections import defaultdict, deque
from typing import List


# def mySort(input: List[str], key: str):
#     mp = defaultdict(int)
#     for i, ch in enumerate(key):
#         mp[ch] = i
#     input.sort(key=lambda word: )

# x <- a

# yz bc
# y <- b


def findKey(input: List[str]) -> str:
    N = len(input)
    LN = 26
    in_degree = [0] * LN
    graph = [[] for _ in range(LN)]
    for i in range(1, N):
        w1, w2 = input[i - 1], input[i]
        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            c1, c2 = w1[j], w2[j]
            if c1 != c2:
                graph[ord(c1) - ord('a')].append(ord(c2) - ord('a'))
                in_degree[ord(c2) - ord('a')] += 1

    dq = deque([i for i, v in enumerate(in_degree) if v == 0])
    ans = ''
    while dq:
        curr = dq.popleft()
        ans += chr(ord('a') + curr)
        for ch in graph[curr]:
            in_degree[ch] -= 1
            if in_degree[ch] == 0:
                dq.append(ch)
    return ans



# def check(input: List[str], expect:st)
if __name__ == '__main__':
    print(findKey(['xyz', 'abc']))
    # print('b' - 'a')