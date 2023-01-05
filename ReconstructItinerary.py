class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = {src:[] for src,_ in tickets}

        tickets.sort()
        for src,dst in tickets:
            adjList[src].append(dst)
        
        answer = ["JFK"]
        def dfs(st):
            # Base Case
            if len(answer) == len(tickets)+1:
                return True
            if st not in adjList:
                return False
            
            for ind,adj in enumerate(adjList[st]):
                adjList[st].pop(ind)
                answer.append(adj)
                if dfs(adj):
                    return True
                adjList[st].insert(ind, adj)
                answer.pop()
            return False
        
        dfs("JFK")
        return answer
    
    '''
    General Idea
        Sort the list of tickets in lexical order and make an adjacent list to return the answer in proper order
        Do recursive DFS, pop the element from adjacent list when you use the edge to get there and put it back to the list
        if it didn't work
    '''