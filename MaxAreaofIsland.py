class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visitedIsland = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        area = 0

        def dfs(i,j):
            islandArea = 0
            visited = set()
            queue = [(i,j)]
            while queue:
                islandArea += 1
                ind = queue.pop()
                nonlocal visitedIsland
                visitedIsland.add(ind)
                visited.add(ind)
                # For each next direction
                for d in dirs:
                    # Get the index
                    nextInd = (ind[0]+d[0], ind[1]+d[1])
                    # Check if index is inside range
                    if -1<nextInd[0]<m and -1<nextInd[1]<n:
                        # Check if it is not visited yet
                        if nextInd not in visited:
                            # Check if it is land or not
                            if grid[nextInd[0]][nextInd[1]]:
                                # If all true, add as next index to go
                                queue.append(nextInd)
                                visited.add(nextInd)

            return islandArea

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visitedIsland:
                    area = max(area, dfs(i,j))
        return area