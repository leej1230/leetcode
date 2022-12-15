class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        num1Ind = 0
        num2Ind = 0
        counter = 0

        if (m+n)%2: # odd case
            while num1Ind<m and num2Ind<n:
                if counter == (m+n)//2:
                    return min(nums1[num1Ind], nums2[num2Ind])
                if nums1[num1Ind] < nums2[num2Ind]:
                    num1Ind += 1
                else:
                    num2Ind += 1
                counter += 1

            if num1Ind == m:
                while counter < (m+n)//2:
                    nums2Ind += 1
                    counter += 1
                return nums2[num2Ind]
            if num2Ind == n:
                while counter < (m+n)//2:
                    nums1Ind += 1
                    counter += 1
                return nums1[num1Ind]
        else: # even case
            while num1Ind<m and num2Ind<n:
                if counter == (m+n)//2:
                    if nums1[num1Ind] < nums2[num2Ind]:
                        middle = nums1[num1Ind]
                        if num1Ind+1 != m:
                            return (middle+min(nums1[num1Ind+1],nums2[num2Ind]))/2
                        else:
                            return (middle+nums2[num2Ind])/2
                    elif nums1[num1Ind] > nums2[num2Ind]:
                        middle = nums2[num2Ind]
                        if num2Ind+1 != n:
                            return (middle+min(nums2[num2Ind+1],nums1[num1Ind]))/2
                        else:
                            return (middle+nums1[num1Ind])/2
                    else:
                        return nums1[num1Ind]

                if nums1[num1Ind] < nums2[num2Ind]:
                    num1Ind += 1
                else:
                    num2Ind += 1
                counter += 1

            if num1Ind == m:
                while counter < (m+n)//2:
                    nums2Ind += 1
                    counter += 1
                return (nums2[num2Ind]+nums2[num2Ind+1])/2
            if num2Ind == n:
                while counter < (m+n)//2:
                    nums1Ind += 1
                    counter += 1
                return (nums1[num1Ind]+nums1[num1Ind+1])/2
        '''
        get m and n
        num1Ind = 0
        num2Ind = 0
        counter = 0
        see if m+n is even or odd
        if odd
            while num1Ind < m and num2Ind < n
                when counter hits (m+n)//2 return min(num1Ind, num2Ind)
                compare num1Ind and num2Ind, increase the one that has less value by 1
            
            either one could be reach to the end
            if num1Ind == m
                while counter < (m+n)//2
                    nums2Ind ++
                return num2Ind
            if num2Ind == n
                while counter < (m+n)//2
                    nums1Ind ++
                return num1Ind
        else (even)
            while num1Ind < m and num2Ind < n
                when counter hits (m+n)//2 
                    if num1Ind < num2Ind
                        middle = num1Ind
                        if num1Ind+1 != m
                            return (middle+min(num1Ind+1,num2Ind))/2
                        else
                            return (middle+num2Ind)/2
                    if num1Ind > num2Ind
                        middle = num2Ind
                        if num2Ind+1 != m
                            return (middle+min(num2Ind+1,num1Ind))/2
                        else
                            return (middle+num1Ind)/2
                    else return that value
                compare num1Ind and num2Ind, increase the one that has less value by 1
            
            either one could be reach to the end
            if num1Ind == m
                while counter < (m+n)//2
                    nums2Ind ++
                return num2Ind+(num2Ind+1)/2
            if num2Ind == n
                while counter < (m+n)//2
                    nums1Ind ++
                return num1Ind+(num1Ind+1)/2

        '''