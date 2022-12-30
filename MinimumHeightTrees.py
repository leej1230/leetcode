class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Make adjacency list
        path = defaultdict(set)
        for edge in edges:
            path[edge[0]].add(edge[1])
            path[edge[1]].add(edge[0])
        
        nodeNum = n
        answer = set(range(n))

        # Find outer nodes (node with one path)
        queue = set()
        for node,neighbor in path.items():
            if len(neighbor) == 1:
                queue.add(node)

        # Do the process until there are last two or one nodes left
        while nodeNum > 2:
            nodeNum -= len(queue)
            newQueue = set()
            while queue:
                curNode = queue.pop()
                answer.remove(curNode)
                # Find adjacent of current Node (there should be only one)
                neighbor = path[curNode].pop()
                # Delete the current Node from that neighbor
                if neighbor in path:
                    path[neighbor].remove(curNode)
                    # If the neighbor now has only 1 path, add to queue
                    if len(path[neighbor]) == 1:
                        newQueue.add(neighbor)
            queue = newQueue
        return list(answer)

        '''
        General Idea
        - We know how many roots ther will be (n possible roots)
        - Make a "graph" using a dictionary
            i.e. for [1,0] -> {1:set(0), 0:set(1)}
        - Starting from root, add all nodes to queue and pop both
          node in dict AND root from connected nodes' sets
        - Repeat the above process with the nodes added in queue
          but do it in BFS (until current queue becomes empty)
          and add 1 to the height and repeat process
        - Save the height to new dictionary
        - After all possible roots has been tested, iterate through
          the dictionary and get minimum, return all nodes that has
          same height as minimum
        class Solution:
            def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
                path = defaultdict(set)
                for edge in edges:
                    path[edge[0]].add(edge[1])
                    path[edge[1]].add(edge[0])
                
                heightTree = defaultdict(int)
                for root in range(n):
                    currentQueue = [root]
                    nextQueue = []
                    pathEdit = copy.deepcopy(path)
                    height = 0

                    while currentQueue:
                        while currentQueue:
                            node = currentQueue.pop()
                            for i in pathEdit[node]:
                                pathEdit[i].remove(node)
                                if len(pathEdit[i]) > 0:
                                    nextQueue.append(i)
                            del pathEdit[node]
                        currentQueue = nextQueue
                        nextQueue = []
                        height += 1
                    
                    heightTree[root] = height
                
                mht = min(heightTree.values())
                answer = []
                for node,h in heightTree.items():
                    if mht == h:
                        answer.append(node)

                return answer

        Solution idea
        - Since there could be one path between any two nodes, we know that the shortest
          distance is found in the centroid of one or two node(s)
        - Rip the outside leaves (node that has only one adjacent node) until we get
          one or two nodes left, and that will be the solution
        '''