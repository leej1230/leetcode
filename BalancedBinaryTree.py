# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = True
        def recursiveDepth(n):
            if n==None:
                return -1
            nonlocal answer
            ld = recursiveDepth(n.left) + 1
            rd = recursiveDepth(n.right) + 1

            if abs(ld-rd) > 1:
                answer = False
            return max(ld,rd)
        
        recursiveDepth(root)
        return answer
        '''
        General idea
            Use the recursive method
            Get the max depth of each left and right
            Compare and if they are different by more than 1
            return false
        '''