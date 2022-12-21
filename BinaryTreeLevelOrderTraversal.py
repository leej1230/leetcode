# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answerList = []
        def recursiveLevel(n,ind):
            if n == None:
                return

            if  ind >= len(answerList):
                answerList.append([n.val])
            else:
                answerList[ind].append(n.val)

            l = recursiveLevel(n.left, ind+1)
            r = recursiveLevel(n.right, ind+1)
            return

        recursiveLevel(root, 0)
        return answerList