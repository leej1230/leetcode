# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answerNode = None
        def recursivelca(n,p,q):
            nonlocal answerNode
            # Base Case
            if answerNode != None:
                return 1
            if n == None:
                return 0
            lFound = recursivelca(n.left,p,q)
            rFound = recursivelca(n.right,p,q)

            if lFound and rFound and answerNode==None:
                answerNode = n
            elif (lFound or rFound) and (n==p or n==q) and answerNode==None:
                answerNode = n
            elif lFound or rFound:
                return 1
            elif n==p or n==q:
                return 1
            return 0

        recursivelca(root,p,q)
        return answerNode
            
        '''
        General idea
            Search by using recursive method, dfs
            Search from bottom up, whenever p and q exists at
            left, right, and itself, return its node
            else return None
        '''