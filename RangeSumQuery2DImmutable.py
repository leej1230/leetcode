class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix.copy()
        self.m = len(matrix)
        self.n = len(matrix[0])
        
        for i in range(1,self.m):
            self.matrix[i][0] += self.matrix[i-1][0]
        for j in range(1,self.n):
            self.matrix[0][j] += self.matrix[0][j-1]
            
        for i in range(1, self.m):
            for j in range(1, self.n):
                self.matrix[i][j] += self.matrix[i-1][j]+self.matrix[i][j-1]-self.matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if(row1 - 1 > -1 and col1 - 1 > -1):
            return self.matrix[row2][col2] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2] + self.matrix[row1-1][col1-1]
        
        if(row1 - 1 < 0 and col1 - 1 < 0):
            return self.matrix[row2][col2]
        
        if(row1 - 1 < 0):
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        
        if(col1 - 1 < 0):
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]