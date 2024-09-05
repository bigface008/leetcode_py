from typing import List

import utils


def compute_lps(pattern: str):
    """
    计算部分匹配表（最长前缀后缀表，LPS数组）
    """
    lps = [0] * len(pattern)
    length = 0  # 记录最长前缀的长度
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text: str, pattern: str):
    """
    在文本text中查找模式pattern，返回匹配的位置
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    i = 0  # text 的索引
    j = 0  # pattern 的索引
    result = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print(f'text={text} pattern={pattern} lps={lps} ans={result}')
    return result


def tst(text: str, pattern: str, expect: List[int]):
    output = kmp_search(text, pattern)
    utils.tst(f'text={text} pattern={pattern}', output, expect)


if __name__ == '__main__':
    # 示例使用
    # text = "ABABDABACDABABCABAB"
    # pattern = "ABABCABAB"
    # positions = kmp_search(text, pattern)
    # print(f"Pattern found at positions: {positions}")
    tst("ABABDABACDABABCABAB", "ABABCABAB", [10])
    tst("ABABDABACDABABCABAB", "ABCABCD", [])
