# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameRecursive(p,q):
            # Base Case
            if p==None or q==None:
                if p==None and q==None:
                    return True
                return False
            
            l = isSameRecursive(p.left, q.left)
            r = isSameRecursive(p.right, q.right)
            if not (l and r):
                return False
            
            return p.val == q.val
            
        return isSameRecursive(p,q)
        '''
        Call the function recursively until either reaches to none
        Base case
            If only one is None return False
            If both is None return True

        Call the function on right side
        Call the function on left side
        if either one returns false than return false

        return the bool of comparing the value of p and q
        '''