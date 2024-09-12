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


def newLinkedList(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    extra = ListNode()
    curr = extra
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return extra.next
