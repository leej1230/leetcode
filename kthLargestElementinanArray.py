class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        def recursiveFind(l,r):
            pivot = nums[r]
            pivotInd = l
            for i in range(l,r):
                if nums[i] <= pivot:
                    # Swap
                    nums[i], nums[pivotInd] = nums[pivotInd], nums[i]
                    pivotInd += 1 
            nums[pivotInd], nums[r] = nums[r], nums[pivotInd]

            if k == pivotInd:
                return nums[pivotInd]
            elif k > pivotInd:
                return recursiveFind(pivotInd+1, r)
            elif k < pivotInd:
                return recursiveFind(l,pivotInd-1)
        return recursiveFind(0, len(nums)-1)
        '''
        Quickselect
        Application of quicksort
        Choose the pivot, right most of the array
        If the number is smaller or eq than the pivot, place on left partition
        If the number is bigger than the pivot, place on right partition
        Exchange the pivot value with leftmost value of right partition
        if pivot index equals to length of array - k return that value
        if pivot index is smaller than len - k recursively call with lhs
        if pivot index is bigger than len - k recursively call with rhs

        Optimized Heap way (O(n*logk) instead of O(n*logn))
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
        '''