class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        b = [0]*(len(nums)+1)
        for n in nums:
            b[n]=1
        for ind,v in enumerate(b):
            if v==0:
                return ind