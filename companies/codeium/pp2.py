# 第二题是给一个document和一个query string，找最先出现的matching的index。
# query里面可以有wildcard，用“*”表示，可以代表任何数量的字符，包括空字符
import utils


def solution(document: str, query: str) -> int:
    patterns = query.split('*')
    NP = len(patterns)
    last = len(document) - 1

    for pi in range(NP - 1, -1, -1):
        pattern = patterns[pi]
        if pi == 0:
            i = document.find(pattern, __end=last)
            if i == -1:
                return -1
            last = i
        i = document.rfind(pattern, __end=last)
        if i == -1:
            return -1
        last = i
    return last


def solution2(document: str, query: str) -> int:
    patterns = query.split('*')
    NP = len(patterns)
    last = len(document) - 1

    def dfs(pi: int) -> int:
        


def check(document: str, query: str, expect: int):
    output = solution(document, query)
    utils.tst(f'document={document} query={query}', output, expect)


if __name__ == '__main__':
    check('abc', 'abc*bcd', 0)
    check('tttabceeebcd', 'abc*bcd', 3)
