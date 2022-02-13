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
