class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Make adjacent list
        adjList = defaultdict(set)
        for equation,value in zip(equations,values):
            # Save (weight of edge, adjacent node)
            adjList[equation[0]].add((value, equation[1]))
            adjList[equation[1]].add((1/value, equation[0]))

        def dfs(st,gl):
            visited = set()
            visited.add(st)
            # Save (current node, value at that point)
            queue = [(st,1)]
            while queue:
                curNode = queue.pop()
                if curNode[0] == gl:
                    return True, curNode[1]
                for adj in adjList[curNode[0]]:
                    if adj[1] not in visited:
                        visited.add(adj[1])
                        queue.append((adj[1], curNode[1]*adj[0]))
            return False, -1

        answer = []
        for query in queries:
            # Whenever either node was NOT in the graph
            if query[0] not in adjList or query[1] not in adjList:
                answer.append(-1)
                continue
            
            isReached,v = dfs(query[0],query[1])
            if isReached:
                answer.append(v)
                # Add new edge for shortcut for next dfs search
                adjList[query[0]].add((v, query[1]))
                adjList[query[1]].add((1/v, query[0]))
            else:
                answer.append(v)

        return answer
        '''
        General Idea
            For each given calculation, convert into variable equal:
                i.e.) for a/b = 2.0 then
                    1. a = 2.0 X b
                    2. b = 1/2 X a
                Based on this conversion, we can form a graph by making variable as a node
                and value as a weight of the edge
                    1. a <-2.0- b
                    2. a -1/2-> b
            Process: There are mainly two processes
                1. Making Graph
                    - adjacent list containing weight of node
                    - (union find may speed up program)
                2. Responding Query
                    - Does both variable exist in the set of nodes in graph
                    - Do dfs from node in first given node
                    - Append the product to answer arr
                    - Maybe adding a new edge might speed up the program
        '''