# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursiveDepth(n):
            if n == None:
                return 0
            
            l = recursiveDepth(n.left) + 1
            r = recursiveDepth(n.right) + 1

            return max(l,r)
        
        return recursiveDepth(root)
        '''
        Make recursive call that receives node
        Base Case
            if left and right is none return 1
        
        +1 with the value from left by recursive call
        +1 with the value from right by recursive call

        return the max of left and right
        '''