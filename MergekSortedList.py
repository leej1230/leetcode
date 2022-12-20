# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numbers = []
        for l in lists:
            A = l
            while A:
                heapq.heappush(numbers, A.val)
                A = A.next
        
        if numbers == []:
            return None
        
        head = ListNode(heapq.heappop(numbers))
        A = head
        while numbers:
            tmp = ListNode(heapq.heappop(numbers))
            A.next = tmp
            A = A.next

        return head