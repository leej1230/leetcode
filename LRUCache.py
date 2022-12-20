class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.storage = {}
        self.capacity = capacity
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.lru.next, self.mru.prev = self.mru, self.lru
    
    def removeNode(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    def appendNode(self, node):
        prv, nxt = self.mru.prev, self.mru
        node.prev = prv
        node.next = nxt
        prv.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.storage:
            self.removeNode(self.storage[key])
            self.appendNode(self.storage[key])
            return self.storage[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.removeNode(self.storage[key])
        self.storage[key] = Node(key,value)
        self.appendNode(self.storage[key])

        if len(self.storage) > self.capacity:
            self.storage.pop(self.lru.next.key)
            self.removeNode(self.lru.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)