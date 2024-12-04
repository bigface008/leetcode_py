from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def tst(desc, output, expect):
    if output == expect:
        print(f'[PASSED] {desc} output={output} expected={expect}')
    else:
        print(f'[FAILED] {desc} output={output} expected={expect}')


def linkedListStr(node: ListNode) -> str:
    ans = ''
    n = node
    while n:
        ans += f'{n.val} -> '
    return ans


def isListEqual(l1: ListNode, l2: ListNode) -> bool:
    return linkedListStr(l1) == linkedListStr(l2)


def newLinkedList(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    extra = ListNode()
    curr = extra
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return extra.next
