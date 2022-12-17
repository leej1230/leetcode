# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive_reverse(prev,curr):
            if curr:
                nex = curr.next
                curr.next = prev
                return recursive_reverse(curr,nex)
            else:
                head = prev
                return head
        return recursive_reverse(None,head)