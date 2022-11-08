class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x, y, word):
            # Base case
            # word is blank ""
            #   return True
            if word == "":
                return True
            
            if not (0 <= x and x < m and 0 <= y and y < n and board[x][y] == word[0]):
                return False
            
            
            # Recursive
            # Make set ((1,0),(-1,0),(0,1),(0,-1))
            neighbors = ((1,0),(-1,0),(0,1),(0,-1))
            # Queue -> Store the places that I need to go
            q = [(x,y)]
            # While queue
            #   curr = pop of queue
            #   Change board word of current coord to #
            #   Look at Neighbors
            #   If neighbor is inside the range
            #       Check the letter is same as word[0]
            #           if dfs(current coordinate, word[1:]):
            #               return True
            # return False
            # while q:
            curr = q.pop()
            keep = board[curr[0]][curr[1]]
            board[curr[0]][curr[1]] = "#"
            # print(board)
            for neighbor in neighbors:
                tmp = (curr[0] + neighbor[0], curr[1] + neighbor[1])
                if dfs(tmp[0], tmp[1], word[1:]):
                        return True
            board[curr[0]][curr[1]] = keep
            
            return False
        
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if (board[i][j] == word[0]):
                    if dfs(i, j, word):
                        return True
        return False