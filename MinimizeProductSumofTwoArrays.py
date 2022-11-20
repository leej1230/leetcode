class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        minheap = nums1
        heapq.heapify(minheap)
        
        maxheap = [(x*-1) for x in nums2]
        heapq.heapify(maxheap)
        
        ans = 0
        while minheap:
            a = heapq.heappop(minheap)
            b = heapq.heappop(maxheap) * -1
            ans += a*b
        return ans