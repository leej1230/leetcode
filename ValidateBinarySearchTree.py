# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        numbers = []
        def recursiveBST(n):
            nonlocal numbers
            if n.left != None:
                l = recursiveBST(n.left)
            numbers.append(n.val)
            if n.right != None:
                r = recursiveBST(n.right)

        recursiveBST(root)
        prev = -float('inf')
        for num in numbers:
            if num <= prev:
                return False
            prev = num
        return True