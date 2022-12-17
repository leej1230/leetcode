# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        deleteNode, nthNextNode = head, head
        while c < n:
            c += 1
            nthNextNode = nthNextNode.next
        
        prevNode = head
        while nthNextNode != None:
            prevNode = deleteNode
            deleteNode = deleteNode.next
            nthNextNode = nthNextNode.next
        
        if deleteNode == head:
            return head.next

        prevNode.next = deleteNode.next

        return head