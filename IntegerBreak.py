class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 1

        def recursiveMaxProduct(n):
            if n in dp:
                return dp[n]
            
            ans = -1
            for i in range(2,n):
                tmp_prod = i * max(n-i, recursiveMaxProduct(n-i))
                ans = max(ans, tmp_prod)
            dp[n] = ans
            return dp[n]
        
        return recursiveMaxProduct(n)
        '''
        Use the memoization dp -> stores max product
        base cases: dp[2]=1

        make a function recursiveMaxProduct(n)
            base case: return dp[n] if exist

            init the ans variable to negative
            Iterate from 2 to n
                tmp_prod = i * max(n-i, recursiveMaxProduct(n-i))
                ans = max(ans, tmp_prod)
            dp[n] = ans
            return dp[n]
        
        return dp[n]
        '''