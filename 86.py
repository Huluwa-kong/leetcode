from linkedlist_helper import *


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        head_sm = tail_sm = None
        head_lg = tail_lg = None
        cur = head
        while cur:
            if cur.val < x:
                if head_sm is None:
                    head_sm = cur
                    tail_sm = head_sm
                else:
                    tail_sm.next = cur
                    tail_sm = cur
            else:
                if head_lg is None:
                    head_lg = cur
                    tail_lg = head_lg
                else:
                    tail_lg.next = cur
                    tail_lg = cur
            cur = cur.next
        if tail_sm is None:
            return head_lg
        if tail_lg is None:
            return head_sm
        tail_sm.next = head_lg
        tail_lg.next = None
        return head_sm


for lst, x in (
        ([1, 4, 3, 2, 5, 2], 3),
        ([2, 1], 2),
        ([], 1),
        ([1, ], 1)
):
    head = build_list(lst)
    print_list(head)
    head = Solution().partition(head, x)
    print_list(head)
    print()
