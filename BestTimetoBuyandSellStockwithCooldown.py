class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = {}
        #Make a hashmap, which will always tell the max profit at (i, buy) or (i, notbuy)

        def dfs(i, buying):
            if i >= l:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                profit = dfs(i+1, not buying) - prices[i]
                cd = dfs(i+1, buying)
                dp[(i, buying)] = max(profit, cd)
            else:
                profit = dfs(i+2, not buying) + prices[i]
                cd = dfs(i+1, buying)
                dp[(i, buying)] = max(profit, cd)
            return dp[(i, buying)]

        return dfs(0, True)
        '''
        Make a hashmap, which will always tell the max profit at (i, buy) or (i, notbuy)

        Make dfs function -> tree that checks every possibility to buy or not buy or sell the stock (i, buying)
            if i is out of range, return 0
            if (i, buying) is in the hashmap -> we already know the max profit that we can earn in that position and state -> return the value for it.

            if buying:
                profit -> next state max profit with not buying - subtracting price i
                cd -> next state max profit with buying
                input value to hashmap -> max between profit or if we didn't buy
            else:
                profit -> next next state max profit not buying + price i
                cd -> next state max profit with buying (not changeing state)
                input value to hashmap ->  max between profit or cd
            return (i, buying)
        
        return dfs(0, true)
        '''