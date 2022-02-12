# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def print_list(head: ListNode):
    cur = head
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
        if cur is not None:
            print('->', end=' ')
    print()


def build_list(values):
    head = None
    prev = None
    for i, v in enumerate(values):
        if i == 0:
            head = ListNode(v)
            prev = head
            continue
        cur = ListNode(v)
        prev.next = cur
        prev = cur
    return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        fast = head

        while fast is not None and n > 1:
            fast = fast.next
            n -= 1
        # illegal input, n is larger than size of list
        if not fast:
            return None
        # remove the first node
        if fast.next is None:
            head = head.next
            return head
        prev = None
        slow = head
        while fast.next is not None:
            fast = fast.next
            prev = head if prev is None else slow
            slow = slow.next
        prev.next = slow.next
        return head


# tests
head = build_list([1, 2, 3, 4, 5])
print_list(head)
head = Solution().removeNthFromEnd(head, 2)
print_list(head)

head = build_list([1])
print_list(head)
head = Solution().removeNthFromEnd(head, 1)
print_list(head)

head = build_list([1, 2])
print_list(head)
head = Solution().removeNthFromEnd(head, 1)
print_list(head)


head = build_list([1, 2])
print_list(head)
head = Solution().removeNthFromEnd(head, 2)
print_list(head)
