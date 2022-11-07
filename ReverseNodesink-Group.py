# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, end):
        curr = head
        nextn = curr.next
        curr.next = end.next
        while curr != end:
            prev = curr
            curr = nextn
            nextn = nextn.next
            curr.next = prev
        return next


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        count = 0
        rev_head = head
        curr = head
        ans = head
        slow = head
        first = True
        for _ in range(k-1):
            if ans == None:
                return head
            ans = ans.next
        while curr:
            count += 1
            if count == k:
                count = 0
                curr = self.reverse(rev_head, curr)
                if first:
                    first = False
                else:
                    slow.next = curr
                rev_head = curr
            else:
                curr = curr.next
        return ans