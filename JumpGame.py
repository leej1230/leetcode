class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        pole = l - 1
        for i in range(l-2, -1, -1):
            if nums[i]+i >= pole:
                pole = i
        return True if pole==0 else False