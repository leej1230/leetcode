"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: #edge case when n==0
            return None

        # Initialize
        nodeDir = {}
        A = head

        # Make Linked List without random
        while A:
            tmpNode = Node(A.val)
            nodeDir[A] = tmpNode

            A = A.next
        
        for original,cp in nodeDir.items():
            if original == None:
                continue
            if original.next == None:
                cp.next = None
            else:
                cp.next = nodeDir[original.next]
            if original.random == None:
                cp.random = None
            else:
                cp.random = nodeDir[original.random]

        return nodeDir[head]
        '''
        Make the array of the Nodes and iterate twice
            1. Store all the copied nodes to dictionary, use original node as a key
            2. iterate through the dictionary and connect next and randoms
        '''