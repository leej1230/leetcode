class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        l = len(prices)
        
        def dfs(i, buying):
            if i >= l:
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            if buying:
                profit = dfs(i+1,not buying) - (prices[i]+fee)
                cd = dfs(i+1,buying)
                dp[(i,buying)] = max(profit, cd)
            else:
                profit = dfs(i+1,not buying) + prices[i]
                cd = dfs(i+1,buying)
                dp[(i,buying)] = max(profit, cd)
            
            return dp[(i,buying)]
        
        return dfs(0,True)