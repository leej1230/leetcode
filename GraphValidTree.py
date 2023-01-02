class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=(n-1):
            return False
        adjList = defaultdict(set)

        # Can A reach to the B?
        def dfs(A,goal):
            visited = set()
            visited.add(A)
            queue = [A]
            while queue:
                cur = queue.pop()
                if cur == goal:
                    return False
                adjs = adjList[cur]
                for adj in adjs:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
            return True

        for edge in edges:
            if not dfs(edge[0], edge[1]):
                return False
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])

        return True
        '''
        General Idea
            Whenever you detect a cycle, return False
            Do dfs without adding the edge
            If one end can reach to the other end before adding that edge, it will make
            a loop
        Process:
            1. Iterate over the edges, and do dfs
            2. If they reach to same node, that means
               there will be a loop when they are connected -> return False
            3. If not, Add the edge to adjacent node
        '''