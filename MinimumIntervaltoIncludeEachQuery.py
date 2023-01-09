class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(queries)
        solutions = {}
        minHeap = []

        i = 0
        n = len(intervals)
        for query in sorted_queries:
            # Add all intervals that contains query with its size
            while i < n and intervals[i][0] <= query:
                heapq.heappush(minHeap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            
            # After everything was added, find answer
            if query not in solutions:
                # Pop the intervals that ends eariler than query
                while minHeap and minHeap[0][1] < query:
                    heapq.heappop(minHeap)
                solutions[query] = minHeap[0][0] if minHeap else -1
        
        answer = []
        for query in queries:
            answer.append(solutions[query])
        return answer