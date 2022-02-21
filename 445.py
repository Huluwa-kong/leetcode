from linkedlist_helper import *


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def inplace_reverse(h: ListNode):
    if not h:
        return h
    new_head = ListNode()
    while h:
        t = h.next
        h.next = new_head.next
        new_head.next = h
        h = t
    return new_head.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = inplace_reverse(l1)
        l2 = inplace_reverse(l2)
        result = ListNode()
        tail = result
        inc = 0
        p1 = l1
        p2 = l2
        while p1 and p2:
            r = p1.val + p2.val + inc
            inc = 0
            if r >= 10:
                inc += 1
                r -= 10
            r = ListNode(r)
            tail.next = r
            tail = r
            p1 = p1.next
            p2 = p2.next
        p = p1 or p2
        while p:
            r = p.val + inc
            inc = 0
            if r >= 10:
                inc += 1
                r -= 10
            r = ListNode(r)
            tail.next = r
            tail = r
            p = p.next
        if inc:
            r = ListNode(inc)
            tail.next = r
        return inplace_reverse(result.next)


for l1, l2 in [
    ([1, ], [9, 9]),
    ([7, 2, 4, 3], [5, 6, 4])
]:
    l1 = build_list(l1)
    l2 = build_list(l2)
    r = Solution().addTwoNumbers(l1, l2)
    print_list(r)
