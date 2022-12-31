class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m = len(rooms)
        n = len(rooms[0])
        """
        idea
        bfs FROM the gate and change the value if the step is lower than what it has atm
        if it can be updated, continue searching
        add index and step in queue
        """

        def bfs(i,j):
            queue = collections.deque()
            queue.append((i,j,0))
            visited = set()
            visited.add((i,j))
            dirs = ((1,0),(-1,0),(0,1),(0,-1))

            while queue:
                cur = queue.popleft()
                for d in dirs:
                    nextind = (cur[0]+d[0], cur[1]+d[1], cur[2]+1)
                    # Check if next is inside the range and not visited yet
                    if -1<nextind[0]<m and -1<nextind[1]<n and (nextind[0],nextind[1]) not in visited:
                        # Check if the room is not obstacle
                        if rooms[nextind[0]][nextind[1]] != -1:
                            # Check if the room has bigger value than what it have on nextind
                            if rooms[nextind[0]][nextind[1]] > nextind[2]:
                                visited.add((nextind[0],nextind[1]))
                                queue.append(nextind)
                                rooms[nextind[0]][nextind[1]] = nextind[2]

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i,j)