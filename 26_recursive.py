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
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        next_node = head.next
        cur.next = next_node.next
        next_node.next = cur
        cur.next = Solution().swapPairs(cur.next)
        return next_node


# tests
head = build_list([1, 2, 3, 4, 5])
print_list(head)
head = Solution().swapPairs(head)
print_list(head)

head = build_list([])
print_list(head)
head = Solution().swapPairs(head)
print_list(head)

head = build_list([1])
print_list(head)
head = Solution().swapPairs(head)
print_list(head)
