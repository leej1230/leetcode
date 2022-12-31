class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        curQueue = []
        time = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    curQueue.append((i,j))
        
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        while curQueue:
            nextQueue = []
            time += 1
            while curQueue:
                curInd = curQueue.pop()
                for d in dirs:
                    nextInd = (curInd[0]+d[0], curInd[1]+d[1])
                    if -1 < nextInd[0] < m and -1 < nextInd[1] < n:
                        if grid[nextInd[0]][nextInd[1]] == 1:
                            grid[nextInd[0]][nextInd[1]] = 2
                            nextQueue.append(nextInd)
            curQueue = nextQueue

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return 0 if time==-1 else time

        '''
        General Idea
            Save index of rotten orange(s) to the queue
            Use two queues
                1. Rotten oranges at same minute
                2. Oranges that will be rotten in next minute (adjacent orange)
            Pop from queue 1 and push valid index to queue 2 and copy queue 2 to queue 1 in the end and repeat the process
            at each process, add 1 to time
            At the end, iterate over whole grid to see if there are left fresh orange
            Return time
        '''