from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[int], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #Pairs of [-count, current time + remain time]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time+n])
            
            if q and q[0][1] >= time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time