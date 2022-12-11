class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        decreaseDeq = collections.deque()
        l,r = 0, 0
        answer = []
        while r < len(nums):
            while decreaseDeq and nums[decreaseDeq[-1]] < nums[r]:
                decreaseDeq.pop()
            decreaseDeq.append(r)

            if decreaseDeq[0] < l:
                decreaseDeq.popleft()
            
            if r+1 >= k:
                answer.append(nums[decreaseDeq[0]])
                l += 1

            r += 1
        return answer

        '''
        make decreasing order deque

        l,r = 0,0
        while r < len(nums)
            while deque and deque[-1] is smaller than current value
                pop the top from deque
            append current value

            if the index of deque[0] is smaller than l
                popleft
            
            if (r+1) >= k
                append leftmost deque to the answer
                l += 1
            r += 1
        '''