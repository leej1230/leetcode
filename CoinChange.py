class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {x:amount+1 for x in range(1,amount+1)}
        dp[0] = 0
        for current_amount in range(1,amount+1):
            for x in coins:
                if (current_amount - x) >= 0:
                    dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - x])
        if dp[amount] == amount+1:
            return -1
        return dp[amount]