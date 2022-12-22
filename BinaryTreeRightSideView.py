# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        def findDepth(n,d):
            if n == None:
                return d
            return max(findDepth(n.right,d+1), findDepth(n.left,d+1))

        d = findDepth(root, 0)

        answer = [0] * d
        def recursiveRight(n,ind):
            # Base Case
            if n == None:
                return
            recursiveRight(n.left,ind+1)
            recursiveRight(n.right, ind+1)
            answer[ind] = n.val

        recursiveRight(root,0)
        return answer
        '''
        General idea
            Find the depth of the tree
            This will be the length of answer array
            Use the recursive method
            Base case: if current node is none
            Check in order of left node and then right node
            Update the value with given index
                * Since the right most side will be visited in the end
                  Simply updating the value will eventually set
                  all array values to right most value
        '''