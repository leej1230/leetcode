class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==1:
            return 0
        parents = [x for x in range(n**2)]
        rank = [1 for _ in range(n**2)]

        # For edges save (time, node A, node B) where node A can connected to node B (A->B) at time
        minHeap = []
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        for i in range(n):
            for j in range(n):
                for d in dirs:
                    a,b = i+d[0],j+d[1]
                    if -1<a<n and -1<b<n:
                        if grid[i][j] > grid[a][b]:
                            heapq.heappush(minHeap, (grid[i][j], (a,b), (i,j)))
        
        while minHeap:
            edge = heapq.heappop(minHeap)
            # Find Parents
            A = edge[1][0]*n+edge[1][1]
            B = edge[2][0]*n+edge[2][1]
            while A != parents[A]:
                A = parents[parents[A]]
            while B != parents[B]:
                B = parents[parents[B]]
            if A==B:
                continue
            if rank[A] > rank[B]:
                rank[A] += rank[B]
                parents[B] = A
            else:
                rank[B] += rank[A]
                parents[A] = B
            # Check if left top and right bottom has same parents == in same tree
            st,gl = parents[0],parents[-1]
            while st != parents[st]:
                st = parents[parents[st]]
            while gl != parents[gl]:
                gl = parents[parents[gl]]
            if st == gl:
                return edge[0]
        '''
        General Idea
            Assume each block is a node it can be connected with square that is at any four directional position that has smaller value than itself
            Do union find and keep track of the parent of (0,0) and (n-1,n-1) whenever they became a same parent, return the time
        '''