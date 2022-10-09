class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j = 0,0
        ind = 0
        tmp = nums1[i:m]
        while i<m and j<n:
            if tmp[i] <= nums2[j]:
                nums1[ind] = tmp[i]
                i += 1
            else:
                nums1[ind] = nums2[j]
                j += 1
            ind += 1
            
        if i==m:
            for a in nums2[j:n]:
                nums1[ind] = a
                ind += 1
        elif j==n:
            for a in tmp[i:m]:
                nums1[ind] = a
                ind += 1