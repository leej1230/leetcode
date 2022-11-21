class Solution:
    def numSquares(self, n: int) -> int:
        PSs = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for ps in PSs:
                if ps > i:
                    break
                dp[i] = min(dp[i], dp[i-ps] + 1)
        return dp[n]