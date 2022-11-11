class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        obstacle = False
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                obstacle = True
            if obstacle:
                obstacleGrid[0][i] = "#"
            else:
                obstacleGrid[0][i] = 1
        
        obstacle = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                obstacle = True
            if obstacle:
                obstacleGrid[i][0] = "#"
            else:
                obstacleGrid[i][0] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j] == 1):
                    obstacleGrid[i][j] = "#"
                    continue
                top = 0 if obstacleGrid[i-1][j]=="#" else obstacleGrid[i-1][j]
                left = 0 if obstacleGrid[i][j-1]=="#" else obstacleGrid[i][j-1]
                obstacleGrid[i][j] = top + left
        
        return obstacleGrid[m-1][n-1]