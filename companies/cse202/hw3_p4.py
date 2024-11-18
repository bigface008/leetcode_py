from typing import List
import numpy as np
import utils


# Given two arrays A[1...n] and B[1...n] whose entries are between 0 to n,
# design an algorithm to output sk for every k between 0 and 2n. sk is defined
# as the number of distinct (i, j) pairs such that A[i] + B[j] = k. Your
# algorithm should have a quasi-linear time complexity, i.e., at most O(nlogn).
def solution3(A: List[int], B: List[int]) -> List[int]:
    N = len(A)
    # Step 1: 构造计数数组 C 和 D
    C = np.zeros(N + 1, dtype=int)
    D = np.zeros(N + 1, dtype=int)

    # 填充计数数组 C 和 D
    for a in A:
        C[a] += 1
    for b in B:
        D[b] += 1

    # Step 2: 使用 FFT 计算卷积
    # 由于我们要计算的范围是 0 到 2n，我们需要将数组扩展到长度 2n+1
    C = np.fft.fft(C, 2 * N + 1)
    D = np.fft.fft(D, 2 * N + 1)

    # Step 3: 计算频域的逐点乘积
    E = C * D

    # Step 4: 逆 FFT 变换
    E = np.fft.ifft(E)

    # Step 5: 提取结果并取整
    # E[k] 是满足 A[i] + B[j] = k 的不同 (i, j) 对的数量
    result = np.round(E.real).astype(int)

    # 返回结果，从 0 到 2n 的每个 k 的计数
    ans = result[:2 * N + 1].tolist()
    print(f'A={A} B={B} ans={ans}')
    return ans


def solution(a: List[int], b: List[int]):
    N = len(a)
    ans = [0] * (2 * N + 1)
    da = [0] * (N + 1)
    db = [0] * (N + 1)
    for x in a:
        da[x] += 1
    for x in b:
        db[x] += 1


def solution2(a: List[int], b: List[int]):
    N = len(a)
    ans = [0] * (2 * N + 1)
    for x in a:
        for y in b:
            ans[x + y] += 1
    return ans


def fake_solution(A: List[int], B: List[int]) -> List[int]
    N = len(A)
    # Step 1: 构造计数数组 C 和 D
    C = np.zeros(N + 1, dtype=int)
    D = np.zeros(N + 1, dtype=int)

    # 填充计数数组 C 和 D
    for a in A:
        C[a] += 1
    for b in B:
        D[b] += 1

    ans = [0] * (2 * N + 1)
    # for j in range(0, )


def tst(a: List[int], b: List[int], expect: int):
    output = solution3(a, b)
    utils.tst(f'test a={a} b={b}', output, expect)


if __name__ == '__main__':
    # 0, 1, 1, 1   0, 1, 1, 1
    # c(sum) = sum(a[k] * b[j - k] for k in [0,j])
    tst([1, 2, 3], [1, 2, 3], [0, 0, 1, 2, 3, 2, 1])
    tst([0, 1, 2], [1, 2, 3], [0, 1, 2, 3, 2, 1, 0])
    tst([2, 2, 2], [1, 2, 3], [0, 0, 0, 3, 3, 3, 0])
    tst([0, 0, 3], [1, 1, 2], [0, 4, 2, 0, 2, 1, 0])
