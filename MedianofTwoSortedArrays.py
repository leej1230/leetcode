class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total//2

        if len(A) > len(B):
            A,B = B,A

        left, right = 0, len(A)-1
        while True:
            AInd = (left+right)//2
            BInd = half - AInd - 2

            ALeft = A[AInd] if AInd > -1 else float('-inf')
            ARight = A[AInd+1] if AInd+1 < len(A) else float('inf')
            BLeft = B[BInd] if BInd > -1 else float('-inf')
            BRight = B[BInd+1] if BInd+1 < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total%2:
                    return min(ARight, BRight)
                else:
                    return (min(ARight, BRight)+max(ALeft,BLeft))/2
            elif ALeft > BRight:
                right = AInd - 1
            else:
                left = AInd + 1



        '''
        Imagine we have merged sorted array,
        to get the median, we have to divide the array into two parts: left and
        right
        Get the left partition by utilizing binary search in one of the array
        combining with another array
        '''