from linkedlist_helper import *

"""
思路：设置两个带表头的虚拟链表分别存放奇数、偶数位节点，遍历原始链表依次放入奇偶链表，
将奇链表尾接上偶链表
"""


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        p_odd = ListNode()
        p_even = ListNode()

        # remember
        h_even = p_even
        h_odd = p_odd

        index = 1
        p = head
        while p is not None:
            tmp = p.next
            p.next = None

            # odd node
            if index % 2:
                p_odd.next = p
                p_odd = p
            # even node
            else:
                p_even.next = p
                p_even = p

            index += 1
            p = tmp
        p_odd.next = h_even.next
        return h_odd.next


for lst in (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [2, 1],
        [],
        [1, ]
):
    head = build_list(lst)
    print_list(head)
    head = Solution().oddEvenList(head)
    print_list(head)
    print()
