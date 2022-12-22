# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodCount = 0
        def recursiveCheck(n,maxNum):
            if n == None:
                return
            nonlocal goodCount
            if n.val >= maxNum:
                goodCount += 1
                recursiveCheck(n.left,n.val)
                recursiveCheck(n.right,n.val)
                return
            else:
                recursiveCheck(n.left,maxNum)
                recursiveCheck(n.right,maxNum)
                return
        recursiveCheck(root,root.val)
        return goodCount