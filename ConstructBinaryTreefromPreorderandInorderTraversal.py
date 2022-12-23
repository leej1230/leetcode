# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        for n in preorder:
            hm[n] = TreeNode(n)

        preInd = 0
        def recursiveConst(left,right):
            if left>right:
                return None
            
            nonlocal preInd
            node = hm[preorder[preInd]]
            val = preorder[preInd]

            preInd += 1

            node.left = recursiveConst(left, inorder.index(val) - 1)
            node.right = recursiveConst(inorder.index(val) + 1, right)
            return node
        
        return recursiveConst(0,len(preorder)-1)
        '''
        Make Treenode for each values and store to hashtable, using
        value as key (it is given that values are unique)

        Recursive Function
        get the node
        base case: length is 1 (maybe 0?)
            return the node
        node.left = recursive call of left side
        node.right = recursive call of right side
        return node

        Find index of preorder[0] in inorder arr
        return recursive(0,foundIndex,len(arr))
        '''