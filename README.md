Me simply keep solving leetcode questions to acquire a ___mega brain___ in a near future
> Rome was not built in a day.

## Bad Questions
1. Matrix Block Sum (1314)
    - Need to get through tedious conditions, do Maximal Square(221) instead
2. Serialize and Deserialize Binary Tree (297)
    - It is not hard if you know basic algorithms of tree. It is hard because you need decent skill with string manipulation.
      Do other questions instead to focus on learn about trees.
3. Design Twitter (355)
    - Don't get me wrong, I like what the question asks. However, it seems like there is slight bug in a leetcode system, that I just could not figure it out even though my idea was all same with the code that works. Solve it, and go over if your idea is correct, don't face with the TypeError thing.

## TIPS
### GIT
- git add *
- git commit -m "commit message here"
- git push

- git log --graph: Shows the history of the repository
- git merge branch-name: Merge branch to current branch
- git checkout branch-name: Switch a branch to branch-name

### Sliding Window Strategy (Q. 424, 76)
- Make window by having left and right pointer (while r < len(sth))
- Problem should be something related to substring
- Think when the window will be valid to the condition that needs to be satisfied to solve the Problem
    - Ex) If the problem asks window to contain same character -> then the window is valid iff there's same characters in the window

### Stack
- Monotonic Decreasing Stack
    - Stack that has numbers in decreasing order
    - If the lower number is added, keep popping until it reaches lower number is found

### Binary Search
- (left+right)//2 to find middle
- Use while loop to do the search: while left<=right

### Linked List
- Know how to get middle of the linked list (move middle by 1 and fast by 2)
- You might want to utilize other data structure algorithm to complete the task (queue, stack...)
- Floyd's Algorithm
    - Alogrithm that identfies a cycle/loop in a linked list
    - Distance between head of list to head of cycle = distance between overlap to head of cycle
    - Method
        1. Initialize fast and slow pointer with head
        2. Move slow pointer by 1, fast pointer by 2
        3. If they overlap (= stops at same node) then there exist a loop in a linked list
            - And can see where the loop starts from by using another pointer from head and find duplicate
        - Proof
            - We know 2*slow = fast
            - fast will loop at least once in the cycle before overlap so it will move p+2c-x
                - where:
                    - c: length of cycle
                    - p: length between head of linked list to head of cycle
                    - x: length between head of cycle to overlap node
            - slow will not loop before overlap: p+c-x
            - So 2(slow) = fast now becomes 2(p+c-x) = p+2c-x
            - p-x = 0 -> p=x
            - Therefore we know: length between head of linked list to head of cycle = 
                length between head of cycle to overlap node

### Trees
- Definition of Tree
    - Graph G is a Tree IF AND ONLY IF:
        1. G is fully connected: from one node, you should be able to go to any nodes that exist in the tree
        2. G contains no cycle: there should be only ONE path to go to one node to other node
- Number of Edge
    - If the there are n nodes in the graph, then number of edge MUST be (n-1)
        - If less, then there will be node(s) that aren't connected
        - If more, there must be a cycle
- If you are familiar with recursive algorithms/coding it won't be too complex to track what's happening
    - I would suggest to practice recursive or dp questions first
- Think about in what order the problems should be solved
    - In left node -> root node -> right node?
    - Deepest left node -> deepest right node -> root node?
- In other word, should the problem solved in bottom-top or top-bottom method that's the first thing to consider
- Usually, to visit all the node, you will have to make a recursive call to call until the node reaches None
- Traversal Algorithm
    - Inorder Traversal
        1. Call inorder with left node
        2. visit the root
        3. Call inorder with right node
    - Preorder Traversal
        1. visit the root
        2. Call preorder with left node
        3. Call preorder with right node
    - Postorder Traversal
        1. Call postorder with left node
        2. Call postorder with right node
        3. visit the root

### Trie / Prefix Tree
- Tree that each node contains a string
- Mainly used for questions that ask to search if the word exist in the data base
- Each node has:
    - Value (string most of the time)
    - next node: Dictionary, use string as key, node as value
    - isEnd: Tells if the Value stored in the node was stored as a word or just a middle of the word
- Solving question Implement Trie (208) is more than enough to understand the concept

### Heap
- Python only has minimum heap
    - heapq.heapify(list_name)
    - heapq.heappush(list_name, value)
    - heapq.heappop(list_name)
    - value can be tuple and will be sorted based on first element
- By making value to negative, it is also possible to make a maximum heap
- No special tips for this, when you start solving, think what needs to be priortize or sorted.

### Backtracking
- Somewhat similar to dp
- This algorithm helps you to identify all possible subset of the array
    - You can partition the array/string in all possible way
- Template
    - For loop that decides the posistion of partition
    - Add partition to array
    - Call the function recursively
    - Remove the partition from array

### Graph
- DFS & BFS
    - The way you write the code is almost similar, difference happens how you pop the queue or call a recursive function
    - Things to prepare
        - set() for keeping visited node (cannot visit same node twice)
        - collection.deque() for saving place that you will visit in future
            - Instead of making queue, you can call the function recusively passing next index or node
        - ((1,0),(-1,0),(0,1),(0,-1)) if grid you need it for visit adjacent space. Yes you have to write this everytime, I know it's time consuming
    - DFS
        - Pop the end from queue, add to visited set
        - From the popped position get next positions 
        - For each positions, make sure if they fit into what you are looking for
        - If they do, add the posisiton in the end of queue or call recursive function with that position
    - BFS
        - Pop the newest element from queue, add to visited set
        - From the popped position get next positions 
        - For each positions, make sure if they fit into what you are looking for
        - If they do, add the posisiton in the end of queue
- Topological Sort
    - Graph must be directed AND no cycle (acyclic graph)
    - Sort the nodes in the order of what should be needs to be processed before reaching a certain node
        - i.e.) if there is graph (handle -> door) topological sort will sort in [handle, door] which tells you handle should be done before going making door
    - Method
        1. For initialization, get all nodes that doesn't have incoming edge and add to queue (if a->b then add a)
        2. Pop left from queue and append to answer list
        3. For each adjacent node of current node pointing at, decrement incoming edge count
        4. If zero, add that node into queue
        5. Repeat the process from #2 until queue becomes empty
        6. In the end if the answer list does NOT have all node it means there is cycle in the graph else the answer list should be sorted in proper order.
- Union Find
    - Algorithm that allows you to identify where the nodes are grouped at
        - In other words, it could show you how many trees are there based on edges
    - Algorithm:
        1. Prepare parents array, each index is representing the node and initially the parent of node should be itself, so value should equal to the index
        2. Prepare rank array, tells you how many children does the node have including itself. Therefore nodes all should have 1 in the beginning
        3. Find number of nodes: to calculate how many trees are there
        4. For each edges (edge given in form of [nodeA, nodeB])
            - Find the parent of nodeA and nodeB by using parents array
            - if nodeA and nodeB has same parent, that means they are already in a same tree, so ignore it and move onto next edge
            - Compare the rank between parent of nodeA and nodeB
            - Parent with BIGGER number of rank will be parent of merged tree so update the parents array's index smaller parent value with parent of bigger tree
            - Update the rank as well
            - Subtract one from Total number of nodes
        5. Number of nodes should now be a number of trees in the graph at this point

### Dynamic Programming (1D 2D)
- Think about this topic when you see a word "max" or "min" in a question sentence
- Draw a tree and identify a subproblem
    - See if anything can be memoized
- Look at the question from different point of view
    - ex) Do we have to make check the string is same with target in every iteration?
            Can that be done by only using index?
- Hash map is BFF with memoization
- Patterns
    - Coin Change
    - 2D
    - 1D
    - Make decision tree and dfs (use memoization)
    - Original formula with subproblems

### Greedy Algorithm
- Most of the time, minimum heap is involved
- Python only has minimum but notice how we can have maximum heap if we multiply -1 to all the values
- Somewhat similar to DP
    - So start from writing a decision tree aka best friend
- Find what can be rejected from consideration (Q.1899)