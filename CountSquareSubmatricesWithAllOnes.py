class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            ans += matrix[i][0]
        for j in range(n):
            ans += matrix[0][j]
        
        if(matrix[0][0]==1):
            ans -= 1
        
        for i in range(1, m):
            for j in range(1, n):
                print(i,j,ans)
                if(matrix[i][j] == 1 and (matrix[i][j-1]>0 and matrix[i-1][j-1]>0 and matrix[i-1][j]>0)):
                    matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
                ans += matrix[i][j]
        return ans