class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # if(len(num) == k):
        #     return "0"
        # s = num
        # for _ in range(k):
        #     minHeap = []
        #     heapq.heapify(minHeap)
        #     for i in range(len(s)):
        #         replaced = (s[0:i]+s[i+1:]).replace(' ','')
        #         if not replaced:
        #             return "0"
        #         tmp = int(replaced)
        #         heapq.heappush(minHeap, tmp)
        #     curr_smallest = heapq.heappop(minHeap)
        #     s = str(curr_smallest)
        # return s
        
        numStack = []
        
        for d in num:
            while k and numStack and numStack[-1] > d:
                numStack.pop()
                k -= 1
            numStack.append(d)
        
        finalStack = numStack[:-k] if k else numStack
        return "".join(finalStack).lstrip('0') or "0"