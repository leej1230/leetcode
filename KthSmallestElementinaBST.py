# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = -1

        def recursiveCount(n):
            nonlocal count,answer
            if n==None or answer!=-1:
                return
            recursiveCount(n.left)

            count += 1
            if count == k:
                answer = n.val

            recursiveCount(n.right)
        
        recursiveCount(root)
        return answer

        '''
        Since the given tree is BST, we know that left most node will
        be the smallest node
        So count from leftmost node and return the kth node
        '''