class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l <= 1:
            return 0
        
        if l == 2:
            return min(cost)
        
        dp = [0]*(l+1)

        for i in range(2,(l+1)):
            dp[i] = min((cost[i-2]+dp[i-2]),(cost[i-1]+dp[i-1]))

        return dp[l]