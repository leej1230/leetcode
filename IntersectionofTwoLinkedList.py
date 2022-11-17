# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        m = 0
        while A:
            m+=1
            A=A.next
        B = headB
        n = 0
        while B:
            n+=1
            B=B.next
            
        A = headA
        B = headB
        while m>n:
            m-=1
            A = A.next
        while m<n:
            n-=1
            B = B.next
        
        
        while A:
            if A==B:
                return A
            A=A.next
            B=B.next
        return None