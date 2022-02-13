func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil{
		return nil
	}
	size := 1
	cur := head
	for ; cur.Next != nil; cur = cur.Next {
		size ++
	}
	tail := cur

	k %= size

	if k == 0{
		return head
	}
	var fast, slow *ListNode
	fast, slow = head, head
	for shift := 0; shift < k - 1; shift ++ {
		fast = fast.Next
	}
	var prev *ListNode = nil
	for ; fast.Next != nil; {
		if prev == nil{
			prev = slow
		} else{
			prev = prev.Next
		}
		fast = fast.Next
		slow = slow.Next
	}
	tail.Next = head
	prev.Next = nil
	head = slow
	return head
}
