class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1 #base case
        
        sorted(coins)
        
        c = coins[-1]
        #base case
        for a in range(1,amount+1):
            if a-c<0:
                dp[a] = 0
            else:
                dp[a] = dp[a-c]
        
        for i in range(len(coins)-2,-1,-1):
            prev_dp = dp
            dp = [0 for _ in range(amount+1)]
            dp[0] = 1
            coin = coins[i]
            for a in range(1,amount+1):
                if a-coin < 0:
                    dp[a] = prev_dp[a]
                else:
                    dp[a] = prev_dp[a] + dp[a-coin]
        return dp[amount]
        '''
        Solve in bottom up method

        make dp array of amount X len(coins) initialized with 0

        Iterate from 0,0 to right corner bottom of dp array
            leftmost column -> if divisble then set 1
            else
                if divisible then add 1 to max of left or up
        '''