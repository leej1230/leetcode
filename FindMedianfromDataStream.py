class MedianFinder:

    def __init__(self):
        self.lhs = [] # max heap
        self.rhs = [] # min heap

    def addNum(self, num: int) -> None:
        n,m = len(self.lhs),len(self.rhs)
        if n==0 and m==0: # Simply add to lhs
            # Do not forget lhs is max heap, we have to push negative value
            heapq.heappush(self.lhs, -num)
            return

        if n <= m: # Add to lhs but make sure everything is sorted
            rhsMin = heapq.heappop(self.rhs)
            if rhsMin < num:
                heapq.heappush(self.lhs, -rhsMin)
                heapq.heappush(self.rhs, num)
            else:
                heapq.heappush(self.lhs, -num)
                heapq.heappush(self.rhs, rhsMin)
            return
        
        if n > m: # Add to rhs to balnace but make sure arrays are sorted
            lhsMax = -heapq.heappop(self.lhs)
            if lhsMax > num:
                heapq.heappush(self.lhs, -num)
                heapq.heappush(self.rhs, lhsMax)
            else:
                heapq.heappush(self.lhs, -lhsMax)
                heapq.heappush(self.rhs, num)
        return

    def findMedian(self) -> float:
        n,m = len(self.lhs),len(self.rhs)
        if n==m:
            return (-self.lhs[0]+self.rhs[0])/2
        return -self.lhs[0]
        
'''
General Idea
    - Imagine there exist sorted array, when you split the array into two
      you can get median just by getting the max from lhs array and getting min
      from rhs array (if there are odd length return max of lhs)
    - Make two heap and everytime you add the number, add in the way that those
      heaps will have same amount of numbers.
        max heap for lhs and min heap for rhs
      If they are already have same amount of numbers, add to lhs (make sure
      they are sorted)
    - When median is asked:
        If lhs and rhs is same, return (lhs[0]+rhs[0])/2
        If different, return lhs[0]
'''

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()