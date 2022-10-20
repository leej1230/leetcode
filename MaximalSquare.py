class Solution:
    def maximalSquare(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = {}
        for x in range(row-1, -1, -1):
            for y in range(col-1, -1, -1):
                if(x == row - 1):
                    down = 0
                else:
                    down = dp[(x+1, y)]
                if(y == col - 1):
                    right = 0
                else:
                    right = dp[(x,y+1)]
                if(x == row -1 or y == col - 1):
                    diag = 0
                else:
                    diag = dp[(x+1, y+1)]
                
                dp[(x,y)] = 0
                if(matrix[x][y] == '1'):
                    dp[(x,y)] = 1 + min(down, right, diag)
        return max(dp.values()) ** 2