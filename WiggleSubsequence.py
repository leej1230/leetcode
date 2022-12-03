class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 1
        down = 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1]>0:
                up = down+1
            if nums[i] - nums[i-1]<0:
                down = up+1
        return max(up,down)
        '''
        Iterate through the array

        if the difference with previous one will be +, then down+1, similar for -

        '''