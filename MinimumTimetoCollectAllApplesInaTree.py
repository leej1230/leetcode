class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(set)
        visited = set()
        visited.add(0)
        for edge in edges:
            if edge[0] in visited:
                adjList[edge[0]].add(edge[1])
            else:
                adjList[edge[1]].add(edge[0])
            visited.add(edge[0])
            visited.add(edge[1])

        def dfs(r):
            # Base Case
            # r does NOT have children node
            if r not in adjList:
                if hasApple[r]:
                    return True,0
                else:
                    return False,0

            timeTaken = 0
            for adj in adjList[r]:
                isApple,time = dfs(adj)
                if isApple:
                    timeTaken += (time+2)
            
            if timeTaken==0 and not hasApple[r]:
                return False,timeTaken
            return True,timeTaken
        
        h,t = dfs(0)
        return t if h else 0
        '''
        General Idea
            divide the question into subproblem and start from bottom of the tree
            If the children has apple, add 2 to the root and repeat its process up until the top
            postorder Traversal
        '''