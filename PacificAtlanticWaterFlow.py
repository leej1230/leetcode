class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def bfs(i,j):
            queue = collections.deque()
            queue.append((i,j))
            visited = set()
            visited.add((i,j))
            dirs = ((1,0),(0,1),(-1,0),(0,-1))
            po = False
            ao = False
            nonlocal answer

            while queue:
                if ao and po:
                    return True
                cur = queue.pop()
                if cur in answer:
                    return True
                for d in dirs:
                    nextInd = (cur[0]+d[0], cur[1]+d[1])
                    if -1<nextInd[0]<m and -1<nextInd[1]<n:
                        if heights[cur[0]][cur[1]] >= heights[nextInd[0]][nextInd[1]]:
                            if nextInd not in visited:
                                visited.add(nextInd)
                                queue.append(nextInd)
                    else:
                        if nextInd[0]<0 or nextInd[1]<0:
                            po = True
                        if nextInd[0]>=m or nextInd[1]>=n:
                            ao = True
            return ao and po

        answer = set()
        for i in range(m):
            for j in range(n):
                if bfs(i,j):
                    answer.add((i,j))
        listedAns = [list(x) for x in answer]
        return listedAns