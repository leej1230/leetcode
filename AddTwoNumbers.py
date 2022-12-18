# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        NextNum = False
        while(first.next is not None and second.next is not None):
            #Add all values to first
            tmp = first.val + second.val
            if(NextNum):
                tmp += 1
                NextNum = False
            if(tmp >= 10):
                tmp -= 10
                NextNum = True
            first.val = tmp
            first = first.next
            second = second.next
        tmp = first.val + second.val
        if(NextNum):
            tmp += 1
            NextNum = False
        if(tmp >= 10):
            tmp -= 10
            NextNum = True
        first.val = tmp
        if(first.next is None):
            first.next = second.next
            while(NextNum and first.next is not None):
                first = first.next
                tmp = first.val + 1
                NextNum = False
                if(tmp >= 10):
                    tmp -= 10
                    NextNum = True
                first.val = tmp
        elif(second.next is None):
            while(NextNum and first.next is not None):
                first = first.next
                tmp = first.val + 1
                NextNum = False
                if(tmp >= 10):
                    tmp -= 10
                    NextNum = True
                first.val = tmp
        #Last Number
        if(NextNum):
            last = ListNode(1)
            first.next = last
        return l1