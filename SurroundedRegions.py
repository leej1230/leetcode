class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        visited = set()

        def dfs(i,j):
            nonlocal visited
            edgeReached = False
            queue = []
            queue.append((i,j))
            visited.add((i,j))
            island = set()
            dirs = ((1,0),(-1,0),(0,1),(0,-1))
            
            while queue:
                cur = queue.pop()
                island.add(cur)

                for d in dirs:
                    nextInd = (cur[0]+d[0], cur[1]+d[1])
                    if -1<nextInd[0]<m and -1<nextInd[1]<n:
                        if board[nextInd[0]][nextInd[1]] == "O" and nextInd not in visited:
                            queue.append(nextInd)
                            visited.add(nextInd)
                    else:
                        edgeReached = True
            
            if not edgeReached:
                for x,y in island:
                    board[x][y] = "X"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    dfs(i,j)