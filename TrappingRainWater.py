class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        leftP = 0
        rightP = len(height)-1
        maxL = height[leftP]
        maxR = height[rightP]
        while leftP < rightP:
            if maxL <= maxR:
                leftP += 1
                maxL = max(maxL, height[leftP])
                answer += maxL - height[leftP]
            else:
                rightP -= 1
                maxR = max(maxR, height[rightP])
                answer += maxR - height[rightP]
        return answer
        '''
        Both of the end won't have "wall" on both side so we can ignore -> if len<3 then return 0

        Iterate thru all the array except both end
            get max in [:i] and [i+1:]
            answer += min(l,r) - height[i] if it is positive else 0
        return answer
        --------Little more optimized way--------------
        Scan through array first and save max value for left and right for each index
        Use equation max(l,r)-height[i] to find solution
        time and space complexity O(n)

        --------Optimized space complexity using two pointers------------
        Based on the equation we have, what we want to know is maximum of each left and right side (and get minimum from it)
        Based on this, we can say that we really do not need maximum of either side
        leftP = 0
        rightP = len-1
        while leftP < rightP:
            maxL = height[leftP]
            maxR = height[rightP]
            if maxL <= maxR:
                tmp = maxL - height[leftP+1]
                if tmp>0:
                    answer += tmp
                leftP += 1
            else:
                tmp = maxR - height[rightP]
                if tmp>0:
                    answer += tmp
                rightP -= 1
        '''