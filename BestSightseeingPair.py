class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0+values[0]]
        ans = -1*float(inf)
        for i in range(1,len(values)):
            dp.append(max(dp[i-1],(i+values[i])))
            ans = max(ans, dp[i-1]+values[i]-i)
        return ans