import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        #Find the day that all the events will end
        event_day = 0
        for e in events:
            event_day = max(event_day,e[1])
        
        events.sort(key = lambda x:(x[0],x[1]))
        minHeap = []
        heapq.heapify(minHeap)
        ans = 0
        event_ind = 0
        n = len(events)

        for day in range(1,event_day+1):
            # Add the end date of events that starts from same days to a minHeap
            while event_ind<n and events[event_ind][0] == day:
                heapq.heappush(minHeap,events[event_ind][1])
                event_ind += 1
            
            # When the first element is smaller than current day, pop it until it gets equal or bigger, bc event is not attendable
            while minHeap and minHeap[0] < day:
                heapq.heappop(minHeap)
            
            # If there is an element in minHeap, that is the event you can attend, pop and add 1 to answer
            if minHeap:
                heapq.heappop(minHeap)
                ans += 1
        return ans