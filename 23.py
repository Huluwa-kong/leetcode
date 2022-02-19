from linkedlist_helper import *
from typing import List, Optional, Tuple


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = ListNode()
        lists = [head for head in lists if head]
        if not lists:
            return None
        tail = new_head
        while True:
            min_index = None
            for i, h in enumerate(lists):
                if h:
                    if min_index is None or h.val < lists[min_index].val:
                        min_index = i
            if min_index is None:
                break
            t = lists[min_index]
            tail.next = t
            lists[min_index] = t.next
            t.next = None
            tail = t
            if lists[min_index] is None:
                lists.pop(min_index)
        return new_head.next


lists = [build_list([1, 3, 5, 7, 9]), build_list([2, 3, 6, 8]), build_list([-1])]
h = Solution().mergeKLists(lists)
print_list(h)
