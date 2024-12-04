import utils
from utils import ListNode, newLinkedList


def solution(l1: ListNode, l2: ListNode) -> ListNode:
    ans = ListNode()
    node = ans
    remain = 0

    n1 = l1
    n2 = l2
    while n1 and n2:
        temp = n1.val + n2.val + remain
        if temp >= 10:
            remain = 1
            node.next = ListNode(temp - 10)
        else:
            remain = 0
            node.next = ListNode(temp)
        node = node.next
        n1 = n1.next
        n2 = n2.next
    while n1:
        temp = n1.val + remain
        if temp >= 10:
            remain = 1
            node.next = ListNode(temp - 10)
        else:
            remain = 0
            node.next = ListNode(temp)
        node = node.next
        n1 = n1.next
    while n2:
        temp = n2.val + remain
        if temp >= 10:
            remain = 1
            node.next = ListNode(temp - 10)
        else:
            remain = 0
            node.next = ListNode(temp)
        node = node.next
        n2 = n2.next
    if remain != 0:
        node.next = ListNode(remain)
    return ans.next


def solution2(l1: ListNode, l2: ListNode) -> ListNode:
    ans = ListNode()
    ans.next = ListNode()
    node = ans.next
    remain = 0

    n1 = l1
    n2 = l2
    while n1 and n2:
        temp = n1.val + n2.val + remain
        if temp >= 10:
            remain = 1
            node.val = temp - 10
        else:
            remain = 0
            node.val = temp
        node.next = ListNode()
        node = node.next
        n1 = n1.next
        n2 = n2.next
    while n1:
        temp = n1.val + remain
        if temp >= 10:
            remain = 1
            node.val = temp - 10
        else:
            remain = 0
            node.val = temp
        node.next = ListNode()
        node = node.next
        n1 = n1.next
    while n2:
        temp = n2.val + remain
        if temp >= 10:
            remain = 1
            node.val = temp - 10
        else:
            remain = 0
            node.val = temp
        node.next = ListNode()
        node = node.next
        n2 = n2.next
    if remain != 0:
        node.val = remain
    return ans.next


def tst(l1: ListNode, l2: ListNode, expect: ListNode):
    output = solution(l1, l2)
    print(utils.isListEqual(output, expect))


if __name__ == '__main__':
    # tst(newLinkedList([2, 4, 3]), newLinkedList([5, 6, 4]), newLinkedList([7, 0, 8]))
    # tst(newLinkedList([0]), newLinkedList([0]), newLinkedList([0]))
    tst(newLinkedList([9, 9, 9, 9, 9, 9, 9]), newLinkedList([9, 9, 9, 9]), newLinkedList([8, 9, 9, 9, 0, 0, 0, 1]))
