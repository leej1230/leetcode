# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middleNode, fastNode = head, head
        while fastNode.next != None and fastNode.next.next != None:
            fastNode = fastNode.next.next
            middleNode = middleNode.next
        
        middle = middleNode.next

        stackNode = collections.deque()
        while middle != None:
            stackNode.append(middle)
            middle = middle.next
        
        A = head
        while stackNode:
            poppedNode = stackNode.pop()
            nextNode = A.next
            A.next = poppedNode
            poppedNode.next = nextNode
            A = nextNode
        A.next = None
        
        return head

        """
        Get the middle node first
            1. while fast.next and fast.next.next is not None
            2. move fast to next next node
            3. move middle to next node


        Stack all the nodes from 1+middle

        while stack is not empty,
            1. Take it out from stack
            2. Keep the next node of current node
            3. Append popped node to current node
            4. Append kept next node to popped node
            5. Current node becomes the kept next node
        
        return head
        """
        