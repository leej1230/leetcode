"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None

        # Initialize
        visited = set()
        queue = [node]
        hashTable = {}

        while queue:
            # Pop the node from queue
            currentNode = queue.pop()
            # Add to visited set as a visited node
            visited.add(currentNode.val)
            # If the currentNode value is not in hashtable, make Node and add to table
            if currentNode.val not in hashTable:
                hashTable[currentNode.val] = Node(val=currentNode.val)

            # For each neighbors:
            for neighbor in currentNode.neighbors:
                # If neighbor was not in hashtable yet, make the node for it and add
                if neighbor.val not in hashTable:
                    hashTable[neighbor.val] = Node(val=neighbor.val)
                
                # If the hashTable's currentNode had empty neighbors, initialize
                # otherwise, append the node if not in neighbor yet
                if hashTable[currentNode.val].neighbors == None:
                    hashTable[currentNode.val].neighbors = [hashTable[neighbor.val]]
                elif hashTable[neighbor.val] not in hashTable[currentNode.val].neighbors:
                    hashTable[currentNode.val].neighbors.append(hashTable[neighbor.val])
                # Append the neighbor to the queue if it has not been visited
                if neighbor.val not in visited:
                    queue.append(neighbor)

        return hashTable[node.val]
        # print(node.val)
        # for neighbor in node.neighbors:
        #     print(neighbor.val)
        # return node
