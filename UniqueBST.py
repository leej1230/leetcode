class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0:1, 1:1, 2:2}
        def uniqueBST(n):
            if n in dp:
                return dp[n]
            for i in range(1,n+1):
                if n not in dp:
                    dp[n] = uniqueBST(i-1)*uniqueBST(n-i)
                else:
                    dp[n] += uniqueBST(i-1)*uniqueBST(n-i)
            return dp[n]
        return uniqueBST(n)
        '''
        with n -> iterate theru and find unique BST for left and right side (current position will be root)
        '''