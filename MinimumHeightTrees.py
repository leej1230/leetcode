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
        '''