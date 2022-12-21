Me simply keep solving leetcode questions to acquire a ___mega brain___ in a near future
> Rome was not built in a day.

## Bad Questions
1. Matrix Block Sum (1314) -> Need to get through tedious conditions, do Maximal Square(221) instead

## TIPS
### GIT
- git add *
- git commit -m "commit message here"
- git push

- git log --graph: Shows the history of the repository
- git merge branch-name: Merge branch to current branch
- git checkout branch-name: Switch a branch to branch-name

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