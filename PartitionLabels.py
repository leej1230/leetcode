class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dp = {}
        for i,l in enumerate(s):
            if l not in dp:
                dp[l] = (i,i)
            else:
                dp[l] = (dp[l][0], i)
        
        minheap = []
        heapq.heapify(minheap)
        for _,val in dp.items():
            heapq.heappush(minheap,val)
        
        partitionRanges = []
        partitionRanges.append(heapq.heappop(minheap))
        while minheap:
            tmp = heapq.heappop(minheap)
            pr = partitionRanges[-1]
            if pr[1]<tmp[0]: #not over lapping
                partitionRanges.append(tmp)
            elif pr[1]<tmp[1]: #Need to update the end
                partitionRanges[-1] = (pr[0], tmp[1])
        
        answer = []
        for t in partitionRanges:
            answer.append(t[1]-t[0]+1)
        
        return answer
        
        '''
        iterate through string
            if letter not in dictionary
                add to dict: (i,i)
            if letter is in dictionary
                change dict[letter][1] = i
        O(n)

        Add all the arrays into minheap from dictionary
        O(26*logn) -> O(logn)

        partitionRanges = []
        pop from heap and add to answer
        Loop until heap becomes empty
            pop from heap
            get answer[-1]
            Check if those two tuples overlap or not (can assume popped one starts later than what you got from answer)
            if overlaps
                change the 2nd value of the tuple in answer
            else
                add popped tuple into answer
        O(26*log(n)) -> O(logn)

        Iterate through partionRanges
            append (second value - first value + 1) to array
        
        return that array
        '''