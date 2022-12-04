class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,v):
            ans = 1
            if (i,j) in dp:
                return dp[(i,j)]
            for d in directions:
                x = i - d[0]
                y = j - d[1]
                if (x>=0 and x<=m-1) and (y>=0 and y<=n-1):
                    if (x,y) not in v:
                        if matrix[x][y] > matrix[i][j]:
                            ans = max(ans, 1+dfs(x,y,v))
            dp[(i,j)] = ans
            return ans
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                v = set()
                dp[(i,j)] = dfs(i,j,v)
        a = -1
        for _,k in dp.items():
            a=max(a,k)
        return a