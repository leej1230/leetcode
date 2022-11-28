class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)== 1:
            return sum(grid[0])
        
        if len(grid[0]) == 1:
            ans = 0
            for g in grid:
                ans += g[0]
            return ans
        
        dp = [0 for _ in range(len(grid[0]))]
        prevDP = [0 for _ in range(len(grid[0]))]
        tmp = 0
        for i in range(len(grid[0])-1,-1,-1):
            tmp += grid[-1][i]
            prevDP[i] = tmp
        
        for i in range(len(grid)-2,-1,-1):
            dp[-1] = prevDP[-1] + grid[i][-1]
            for j in range(len(grid[0])-2,-1,-1):
                dp[j] = grid[i][j] + min(prevDP[j], dp[j+1])
            prevDP = dp
        return dp[0]
        '''
        grid is 1d -> simply return the sum

        from here we will be getting grid 2d
        dp -> initialized array with 0 that has a length of n
        prevDP -> array that has iterated from bottom to top and initialized with sum until there

        for 1 above the bottom of grid row to the top
            initialize first number with dp[0] = grid[current position][0]+prevDP[0]
            for from 1 before bottom of row to top
                get minimum from right and down and add with grid set to dp
            
            write over prevDP with dp since we don't need it anymore
        
        return dp[0]
        '''