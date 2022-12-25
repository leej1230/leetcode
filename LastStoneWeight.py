class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = []
        for stone in stones:
            heapq.heappush(stoneHeap,(-1*stone))
        
        while len(stoneHeap) > 1:
            A = -1*heapq.heappop(stoneHeap)
            B = -1*heapq.heappop(stoneHeap)
            if A==B:
                continue
            heapq.heappush(stoneHeap, -1*abs(A-B))

        return -stoneHeap[0] if len(stoneHeap) else 0