class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        firstRow = None
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i==0:
                        firstRow = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        
        for i in range(1,n):
            if matrix[i][0] == 0:
                matrix[i] = [0]*m
        
        for j in range(m):
            if matrix[0][j] == 0:
                for k in range(n):
                    matrix[k][j] = 0

        if firstRow!=None:
            matrix[0] = [0]*m