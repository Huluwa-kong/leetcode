from typing import Optional
from linkedlist_helper import *

"""
做的时候没有理清思路，考虑好详细的策略
TODO: 仅扫描一次的solution
"""


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        # get the size and tail of list
        sz = 1
        cur = head
        while cur.next is not None:
            cur = cur.next
            sz += 1
        tail = cur

        k %= sz

        if k == 0:
            return head

        fast = head
        slow = head
        shift = 0
        while shift < k - 1:
            fast = fast.next
            shift += 1
        prev = None
        while fast.next:
            prev = slow if prev is None else prev.next
            fast = fast.next
            slow = slow.next

        tail.next = head
        prev.next = None
        head = slow
        return head


for lst, k in (
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3),
        ([0, 1, 2], 4),
        ([0, 1, 2], 1),
        ([0, 1, 2], 2),
        ([0, 1, 2], 3),
        ([], 3),
        ([1], 10)
):
    head = build_list(lst)
    print_list(head)
    head = Solution().rotateRight(head, k)
    print_list(head)
    print()
