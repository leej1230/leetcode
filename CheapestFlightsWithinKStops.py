class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialization for Dijkstra
        pathWeight = [float('inf') for _ in range(n)]
        pathWeight[src] = 0
        remainingNode = collections.deque([(0,src,0)])

        # Adjacent List
        adjList = defaultdict(set)
        adjMatrix = [[0 for _ in range(n)] for _ in range(n)]
        for flight in flights:
            adjList[flight[0]].add(flight[1])
            adjMatrix[flight[0]][flight[1]] = flight[2]
        
        while remainingNode:
            curNode = remainingNode.popleft()
            for adjNode in adjList[curNode[1]]:
                cost = curNode[0] + adjMatrix[curNode[1]][adjNode]
                if pathWeight[adjNode] > cost and curNode[2] <= k:
                    pathWeight[adjNode] = cost
                    remainingNode.append((cost, adjNode, curNode[2]+1))

        return -1 if pathWeight[dst]==float('inf') else pathWeight[dst]


        '''
        General Idea
            Dijkstra Theorem
            - Imagine src is the starting point and price as a time taken to reach that node
            - Find the fastest way to reach the dst within k
        '''