class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        
        visited = {}
        answer = []
        def dfs(st):
            if st in visited:
                return visited[st]
            
            visited[st] = True
            for adj in adjList[st]:
                if dfs(adj):
                    return True
            visited[st] = False
            answer.append(st)
        
        for c in adjList:
            if dfs(c):
                return ""
        
        answer.reverse()
        return "".join(answer)