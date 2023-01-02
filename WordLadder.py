class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList):
            return 0
        # At this point, it is guranteed that wordList has endWord

        # Making adj list
        adjList = defaultdict(set)
        for word in wordList:
            for i in range(len(beginWord)):
                adjList[word[:i] + "*" + word[i+1:]].add(word)
        # print(adjList)

        def bfs(st):
            queue = collections.deque([(st,1)])
            visited = set()
            visited.add(st)

            while queue:
                curWord,level = queue.popleft()
                for i in range(len(beginWord)):
                    adjs = adjList[curWord[:i] + "*" + curWord[i+1:]]
                    for adj in adjs:
                        if adj not in visited:
                            if adj == endWord:
                                return level
                            queue.append((adj,level+1))
                            visited.add(adj)
            # Couldn't reach endWord
            return -1

        shortestPath = bfs(beginWord)
        return shortestPath+1 if shortestPath!=-1 else 0
        '''
        General Idea
            Make graph of words that adjacent nodes has only one difference in words
            and do BFS to get shortest path
        Problem: Too heavy to calculate since you have to do double for loop to create
                 a dictionary
        Code:
        if endWord not in set(wordList):
            return 0
        # At this point, it is guranteed that wordList has endWord

        def onedif(A,B):
            noDif = True
            for one,two in zip(A,B):
                if one != two and noDif:
                    noDif = False
                elif one != two:
                    return False
            return True

        # Making adj list
        adjList = defaultdict(set)
        allWords = wordList + [beginWord]
        for ind,word in enumerate(allWords):
            for s in (allWords[:ind]+allWords[ind+1:]):
                if onedif(word,s):
                    adjList[word].add(s)
                    adjList[s].add(word)
        # print(adjList)

        # Return if node of endWord is unreachable
        if len(adjList[endWord]) == 0:
            return 0

        def bfs(st):
            queue = [st]
            visited = set()
            visited.add(st)
            answer = 0
            while queue:
                nextQueue = []
                answer += 1
                while queue:
                    cur = queue.pop()
                    for adj in adjList[cur]:
                        if adj not in visited:
                            if adj == endWord:
                                return answer
                            nextQueue.append(adj)
                            visited.add(adj)
                queue = nextQueue
            # Couldn't reach endWord
            return -1

        shortestPath = bfs(beginWord)
        return shortestPath+1 if shortestPath!=-1 else 0

        Optimal solution:
            The basic idea is same, but the difference is that you add words as
            an adjacent list and key be the word but with one blank such as "d*g"
            In this case, there is no need to check what word is adjacent to what
        '''