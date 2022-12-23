# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = -float('inf')

        def recursiveMax(n):
            if n == None:
                return 0
            
            leftMax = recursiveMax(n.left)
            rightMax = recursiveMax(n.right)

            nonlocal answer
            answer = max(answer, n.val, n.val+leftMax+rightMax, n.val+leftMax, n.val+rightMax)

            return max(n.val, n.val+leftMax, n.val+rightMax)
        
        recursiveMax(root)
        return answer


        '''
        General Idea
            Use the buttom-up method and solve the subproblems
            from nodes in the bottom
            Initialize answer with -inf
            Recursively:
                1. Base case: if node is none return
                2. recursive call with left node
                3. recursive call with right node
                4. answer = max(answer, left + right)
                5. return max(current, left+current, right+current)
            return answer
        '''