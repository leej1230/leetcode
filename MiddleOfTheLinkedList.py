class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head.next == None):
            return head

        slow, fast = head, head
        while(fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next

        if(fast.next != None):
            return slow.next
        return slow