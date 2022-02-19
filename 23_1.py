from linkedlist_helper import *
from typing import List, Optional, Tuple


class MinHeap:
    def __init__(self):
        self.heap: List[ListNode] = []

    def _adjust_bottom_up(self, index):
        while index > 0:
            # !!!!!
            parent = (index - 1) // 2
            if self.heap[index].val < self.heap[parent].val:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _adjust_top_down(self, index):
        while index * 2 + 1 < self.size():
            min_child = index * 2 + 1
            right = min_child + 1
            if right < self.size() and self.heap[right].val < self.heap[min_child].val:
                min_child = right
            if self.heap[min_child].val <= self.heap[index].val:
                self.heap[index], self.heap[min_child] = self.heap[min_child], self.heap[index]
                index = min_child
            else:
                break

    def push(self, h: ListNode):
        self.heap.append(h)
        self._adjust_bottom_up(len(self.heap) - 1)

    def pop(self) -> ListNode:
        assert not self.empty()
        h = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return h

        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self._adjust_top_down(0)
        return h

    def empty(self) -> bool:
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def check(self):
        for index in range(len(self.heap) // 2 + 1):
            left = index * 2 + 1
            right = left + 1
            if left < self.size() and self.heap[left].val < self.heap[index].val:
                raise AssertionError(f'{index} {self.heap[left].val} >= {self.heap[index].val}')
            if right < self.size() and self.heap[right].val < self.heap[index].val:
                raise AssertionError(f'{index} {self.heap[right].val} >= {self.heap[index].val}')

    def __str__(self):
        return str(self.heap)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = ListNode()
        tail = new_head
        heap = MinHeap()
        for h in lists:
            if h:
                heap.push(h)
        while not heap.empty():
            h = heap.pop()
            tail.next = h

            if h.next:
                heap.push(h.next)
            tail = h
            h.next = None

        return new_head.next


ll = [[-4], [-10, -6, -6], [0, 3], [2], [-10, -9, -8, 3, 4, 4], [-10, -10, -8, -6, -4, -3, 1], [2], [-9, -4, -2, 4, 4],
      [-4, 0]]
lists = [build_list(e) for e in ll]
h = Solution().mergeKLists(lists)
print_list(h)
