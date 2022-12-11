class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currentMinimumVal = float('inf')
        self.stackSize = 0
        self.topIndex = 0
        '''
        make global empty stack
        make global empty stack to keep track minimum
        make global variable keep minimum value (initialize with inf)
        make global variable that keeps track of size of the stack(initialize with 0)
        make global variable that keeps current top index (initialize with 0)
        '''

    def push(self, val: int) -> None:
        if self.topIndex == 0 or val < self.minStack[self.topIndex-1]:
            self.currentMinimumVal = val
        if self.stackSize == self.topIndex:
            self.stack.append(val)
            self.minStack.append(self.currentMinimumVal)
            self.stackSize += 1
        else:
            self.stack[self.topIndex] = val
            self.minStack[self.topIndex] = self.currentMinimumVal

        self.topIndex += 1
        '''
        if size == 0:
            minval = stack[0]
        else:
            if val < stack[top_ind-1]
                minval = val
        if size == top_ind
            append val to stack
            minstack.append(minval)
        else
            stack[top_ind] = val
            minstack[top_ind] = minval
        size += 1
        top_ind += 1
        '''
        
    def pop(self) -> None:
        self.topIndex -= 1
        #if self.topIndex == 0
        if self.topIndex > 0:
            self.currentMinimumVal = self.minStack[self.topIndex-1]
        '''
        top_ind -= 1
        size -= 1
        '''

    def top(self) -> int:
        return self.stack[self.topIndex-1]
        '''
        return stack[top_ind]
        '''

    def getMin(self) -> int:
        return self.minStack[self.topIndex-1]
        '''
        return minstack[top_ind]
        '''


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()