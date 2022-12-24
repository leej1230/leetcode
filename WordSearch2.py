class TrieNode:
    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.nextNode = {}

class Solution:
    def __init__(self):
        self.root = TrieNode(None)
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Make Trie with given words
        for word in words:
            prevNode = self.root
            for char in word:
                if char not in prevNode.nextNode:
                    new_node = TrieNode(char)
                    prevNode.nextNode[char] = new_node
                prevNode = prevNode.nextNode[char]
            prevNode.isEnd = True
        

        answer = set()
        visit = set()
        n,m = len(board), len(board[0])
        def recursiveSearch(i,j,node,w):
            if 0>i or i>=n or 0>j or j>=m or (i,j) in visit or board[i][j] not in node.nextNode:
                return
            w += board[i][j]
            currentNode = node.nextNode[board[i][j]]
            visit.add((i,j))
            if currentNode.isEnd:
                answer.add(w)

            recursiveSearch(i+1,j,currentNode,w)
            recursiveSearch(i-1,j,currentNode,w)
            recursiveSearch(i,j+1,currentNode,w)
            recursiveSearch(i,j-1,currentNode,w)
            visit.remove((i,j))

        for i in range(n):
            for j in range(m):
                recursiveSearch(i,j,self.root,"")
        return list(answer)