class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        heapq.heapify(self.queue)
        self.k = k
        while len(self.queue) > k:
            heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        if len(self.queue) > self.k:
            heapq.heappop(self.queue)
        return self.queue[0]
'''
General idea
    Its a kth LARGEST element that we have to find.
        Ex) If we have 1,2,3 then 3 is the first largest, 1 is third largest
    To find that we can place last k largest elements in the queue
    and return 0th index using heap
'''

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)