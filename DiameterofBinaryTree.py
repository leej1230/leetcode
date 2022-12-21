# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def recursiveDepth(n):
            # Base Case
            if n == None:
                return -1
            
            nonlocal answer
            
            l = recursiveDepth(n.left) + 1
            r = recursiveDepth(n.right) + 1
            answer = max(answer,l+r)
            return max(l,r)
        
        recursiveDepth(root)
        return answer