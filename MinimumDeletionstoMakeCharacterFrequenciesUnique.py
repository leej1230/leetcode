class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        l = {}
        for ch in s:
            if ch not in l:
                l[ch] = -1
            else:
                l[ch] -= 1
        minHeapA = []
        heapq.heapify(minHeapA)

        for val in l.values():
            heapq.heappush(minHeapA,val)

        while len(minHeapA) > 1:
            top = -1 * heapq.heappop(minHeapA)
            peek_top = -1 * minHeapA[0]
            if (top == peek_top):
                top -= 1
                ans += 1
                if(top != 0):
                    heapq.heappush(minHeapA,(-1 * top))
            
        return ans