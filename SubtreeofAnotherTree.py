# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recursiveCheck(n,s):
            if n == None and s == None:
                return True
            if n == None or s == None:
                return False
            return n.val == s.val and recursiveCheck(n.left,s.left) and recursiveCheck(n.right, s.right)

        def recursiveTrace(n):
            if n == None:
                return False

            if recursiveCheck(n,subRoot):
                return True
            
            return recursiveTrace(n.left) or recursiveTrace(n.right)

        return recursiveTrace(root)