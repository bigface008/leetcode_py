from itertools import groupby


def solution(name: str, typed: str) -> bool:
    it1 = [(k, len(list(v))) for k, v in groupby(name)]
    it2 = [(k, len(list(v))) for k, v in groupby(typed)]
    if len(it1) != len(it2):
        return False
    for (k1, v1), (k2, v2) in zip(it1, it2):
        if k1 != k2 or v1 > v2:
            return False
    return True


def tst(name: str, typed: str, expect: bool):
    print(solution(name, typed) == expect)


if __name__ == '__main__':
    tst("alex", "aaleex", True)
    tst("saeed", "ssaaedd", False)