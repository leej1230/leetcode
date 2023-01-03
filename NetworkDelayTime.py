class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pathWeight = [float('inf') for _ in range(n)]
        pathWeight[k-1] = 0
        remainingNode = collections.deque([(k,pathWeight[k-1])])

        adjList = defaultdict(set)
        adjMatrix = [[0 for _ in range(n)] for _ in range(n)]
        for time in times:
            adjList[time[0]-1].add(time[1])
            adjMatrix[time[0]-1][time[1]-1] = time[2]
        
        while remainingNode:
            curNode = remainingNode.popleft()
            for adjNode in adjList[curNode[0]-1]:
                cost = curNode[1] + adjMatrix[curNode[0]-1][adjNode-1]
                if pathWeight[adjNode-1] > cost:
                    pathWeight[adjNode-1] = cost
                    remainingNode.append((adjNode,cost))
        
        return -1 if max(pathWeight)==float('inf') else max(pathWeight)