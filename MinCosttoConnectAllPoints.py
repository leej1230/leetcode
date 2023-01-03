class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(set)
        for i in range(len(points)):
            adjList[i] = set(list(range(i))+list(range(i+1,len(points))))
        
        minHeap = [(0,0)]
        visited = set()
        answer = 0

        while len(visited) < len(points):
            current = heapq.heappop(minHeap)
            if current[1] not in visited:
                visited.add(current[1])
                answer += current[0]
                for adj in adjList[current[1]]:
                    if adj not in visited:
                        A = points[current[1]]
                        B = points[adj]
                        calc = abs(A[0]-B[0]) + abs(A[1]-B[1])
                        heapq.heappush(minHeap, (calc, adj))

        return answer