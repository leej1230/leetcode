class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        answerLeft = 0
        answerRight = k-1
        prevDist = float('inf')

        newDist = 0
        l,r = 0,0
        while r < len(arr):

            newDist += abs(arr[r] - x)

            # Window size equals to k
            if r-l+1 == k:
                if prevDist>newDist:
                    prevDist = newDist
                    answerLeft = l
                    answerRight = r

                newDist -= abs(arr[l] - x)
                l += 1
                r += 1
            else:
                r += 1


        return arr[answerLeft:answerRight+1]

        '''
        General Idea
            - Slide the window with size of k all the way till the outside
              of the range
            - Get the total distances from the window
            - When the distance is minimum, store the window to return in
              the end
            - Slide the whole window with updating total distances
        '''