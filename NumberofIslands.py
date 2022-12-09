class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            queue = []
            queue.append((i,j))
            fourDirections = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                currentCoord = queue.pop()
                grid[currentCoord[0]][currentCoord[1]] = "#"
                for direction in fourDirections:
                    nextCoord = (currentCoord[0]+direction[0], currentCoord[1]+direction[1])
                    if nextCoord[0]>-1 and nextCoord[0]<m and nextCoord[1]>-1 and nextCoord[1]<n:
                        if grid[nextCoord[0]][nextCoord[1]]=="1":
                            queue.append(nextCoord)
        
        islandCounter=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islandCounter+=1
                    dfs(i,j)
        return islandCounter
        '''
        dfs(i,j):
            Make queue
            add (i,j) to queue
            fourDirections = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                currentCoord = pop from queue
                change the grid's currentCoord to '#'
                for direction in fourDirections:
                    nextCoord = add direction to currentCoord
                    if the nextCoord is in bound:
                        if the nextCoord is 1:
                            add nextCoord to the queue

        islandCounter = 0
        Iterate through all the 2d array elements
            if the element is 1
                add 1 to the counter and send coordinate to the dfs
        '''