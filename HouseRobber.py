class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if(l == 1):
            return nums[0]
        if(l == 2):
            return max(nums[0],nums[1])
        nums[2] += nums[0]
        for i in range(3, l):
            nums[i] += max(nums[i-2],nums[i-3])
        return max(nums[l-1],nums[l-2])