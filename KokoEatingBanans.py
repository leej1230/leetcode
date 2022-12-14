class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        possibleRate = range(1,max(piles)+1)
        answer = -1

        left, right = 0, max(piles)-1
        while left <= right:
            middle = int((left+right)/2)
            rate = possibleRate[middle]
            hTaken = 0
            for i in piles:
                hTaken += ceil(i/rate)
                if hTaken > h:
                    break
            if hTaken > h:
                left = middle + 1
            else:
                right = middle - 1
                answer = rate
        
        return answer
        '''
        [idea]
        the brute force way to solve this problem is to solve the problem by trying all the
        possible answers and check if it works.
        Possible answers in this context would be range from (1 to maximium value in piles)
            To develop this brute force way to optimal way is to use binary search in the range
            Pick number from the list and see if that can be the answer
            if Koko cannot finish in "h" -> go search for bigger number
            if Koko finishes in "h" -> go search for smaller number
        '''