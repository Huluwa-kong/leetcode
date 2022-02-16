from linkedlist_helper import *
from typing import Optional

# todo: 优化，空间复杂度为1，交换节点而非值


def get_size(head: ListNode) -> int:
    sz = 0
    while head:
        head = head.next
        sz += 1
    return sz


def find_mid(head: ListNode, sz: int) -> ListNode:
    index = sz // 2
    mid = head
    while index > 0:
        assert mid is not None, f'Error, node is None.'
        mid = mid.next
        index -= 1
    return mid


def merge_sort(head: ListNode, sz: int):
    if sz <= 1:
        return
    mid = find_mid(head, sz)
    left_size = sz // 2
    right_size = sz - left_size
    merge_sort(head, left_size)
    merge_sort(mid, right_size)
    # merge two parts of list node
    li = 0
    ri = 0
    rp = mid
    lp = head
    vals = []
    while li < left_size and ri < right_size:
        if lp.val <= rp.val:
            li += 1
            vals.append(lp.val)
            lp = lp.next
        else:
            ri += 1
            vals.append(rp.val)
            rp = rp.next
    while li < left_size:
        vals.append(lp.val)
        li += 1
        lp = lp.next
    while ri < right_size:
        vals.append(rp.val)
        rp = rp.next
        ri += 1
    cur = head
    for e in vals:
        cur.val = e
        cur = cur.next


class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap value, not node

        Algorithm
        sz = getSize(head)
        if sz <= 1:
          return head ?
        mid = findMid(head, sz)
        sortList(head, mid - 1?)
        sortList(mid)

        mergeList(head, mid)
        """
        sz = get_size(head)
        if sz <= 1:
            return head
        merge_sort(head, sz)
        return head


ll = build_list([4, 3, 2, 1])
print_list(ll)
Solution().sortList(ll)
print_list(ll)

ll = build_list([1, 3, 5, 7, 2, 4, 6, 8])
print_list(ll)
Solution().sortList(ll)
print_list(ll)

