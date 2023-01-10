class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        i,j = 0,0
        wallTop,wallBot,wallLeft,wallRight = 0,m,0,n

        answer = []

        while wallLeft < wallRight and wallTop < wallBot:
            for i in range(wallLeft,wallRight):
                answer.append(matrix[wallTop][i])
            wallTop += 1
            
            for i in range(wallTop,wallBot):
                answer.append(matrix[i][wallRight-1])
            wallRight -= 1

            if not (wallLeft < wallRight and wallTop < wallBot):
                break

            for i in range(wallRight-1,wallLeft-1,-1):
                answer.append(matrix[wallBot-1][i])
            wallBot -= 1
            
            for i in range(wallBot-1,wallTop-1,-1):
                answer.append(matrix[i][wallLeft])
            wallLeft += 1
            
        return answer