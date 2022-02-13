from linkedlist_helper import *


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
