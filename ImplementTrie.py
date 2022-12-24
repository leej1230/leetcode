class TrieNode:
    def __init__(self, val):
        self.val = val
        self.key = -1
        self.nextNode = {}

class Trie:

    def __init__(self):
        self.root = TrieNode(None)
        self.key = 1
        

    def insert(self, word: str) -> None:
        prevNode = self.root
        for i in range(len(word)):
            if i != len(word)-1:
                node = TrieNode(word[:i+1])
                if word[:i+1] not in prevNode.nextNode:
                    prevNode.nextNode[word[:i+1]] = node
                prevNode = prevNode.nextNode[word[:i+1]]
            else:
                node = TrieNode(word)
                node.key = self.key
                self.key += 1
                if word not in prevNode.nextNode:
                    prevNode.nextNode[word] = node
                else:
                    prevNode.nextNode[word].key = node.key
                prevNode = prevNode.nextNode[word]
        
    def search(self, word: str) -> bool:
        prevNode = self.root
        for i in range(len(word)):
            if word[:i+1] not in prevNode.nextNode:
                return False
            else:
                prevNode = prevNode.nextNode[word[:i+1]]
        if prevNode.key>0:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        prevNode = self.root
        for i in range(len(prefix)):
            if prefix[:i+1] not in prevNode.nextNode:
                return False
            else:
                prevNode = prevNode.nextNode[prefix[:i+1]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)