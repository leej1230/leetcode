class TrieNode:
    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.nextNode = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        prevNode = self.root
        for i in range(len(word)):
            if i != len(word)-1:
                node = TrieNode(word[:i+1])
                if word[:i+1] not in prevNode.nextNode:
                    prevNode.nextNode[word[:i+1]] = node
                prevNode = prevNode.nextNode[word[:i+1]]
            else:
                node = TrieNode(word)
                node.isEnd = True
                if word not in prevNode.nextNode:
                    prevNode.nextNode[word] = node
                else:
                    prevNode = prevNode.nextNode[word]
                    prevNode.isEnd = True

    def search(self, word: str) -> bool:
        def recursiveSearch(n,l):
            if len(l)==0:
                return n.isEnd
            if l[0] == '.':
                for key,node in n.nextNode.items():
                    if recursiveSearch(node, l[1:]):
                        return True
            else:
                for key,node in n.nextNode.items():
                    if l[0] == key[-1]:
                        if recursiveSearch(node, l[1:]):
                            return True
            return False
        return recursiveSearch(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)