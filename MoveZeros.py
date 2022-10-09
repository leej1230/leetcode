class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ind = len(nums) - 1
        for i in range(ind,-1,-1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)