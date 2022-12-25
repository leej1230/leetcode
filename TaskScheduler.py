class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0: return len(tasks)
        hm = {}
        taskHeap = []
        for task in tasks:
            if task not in hm:
                hm[task] = 1
            else:
                hm[task] += n+1
            heapq.heappush(taskHeap, hm[task])
            
        time = 0
        while taskHeap:
            time += 1
            if taskHeap[0] > time:
                continue
            heapq.heappop(taskHeap)
        return time