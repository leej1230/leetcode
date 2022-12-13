class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = collections.deque()

        answer = -1

        for index, height in enumerate(heights):
            lastIndex = -1
            while stack and stack[-1][1] > height:
                recentHeight = stack.pop()
                lastIndex = recentHeight[0]
                answer = max(answer, (index - recentHeight[0])*recentHeight[1])
            
            if lastIndex != -1:
                stack.append((lastIndex, height))
            else:
                stack.append((index, height))
        
        while stack:
            recentHeight = stack.pop()
            answer = max(answer, (len(heights) - recentHeight[0])*recentHeight[1])

        return answer

        '''
        Use monotonic increasing stack to see if the rectangle can be "extended" or not
        
        initialize answer with -1

        for ind, h in enumerate(heights):
            last index = -1
            while the stack is NOT empty AND the top is higher than h
                pop the top from stack
                last index = top[index]
                answer = max(answer, (ind-top[index])*top[height])
            
            if last index != -1
                add (lastindex, h) to the stack
            else
                add (ind,h) to the stack
        
        while stack is NOT empty
            pop from top of the stack
            answer = max(answer, (len(heights)-top[index])*top[height])

        return answer

        '''