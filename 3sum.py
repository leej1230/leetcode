class Solution:
    def twoSum(self, nums:List[int], ind:int, ans:List[List[int]]):
        seen = set()
        j = ind + 1
        while j < len(nums):
            complement = -nums[ind] - nums[j]
            if complement in seen:
                ans.append([nums[ind], nums[j], complement])
                while j + 1<len(nums) and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])
            j += 1

    def threeSum(self, nums:List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for ind, num in enumerate(nums):
            if(num > 0):
                break
            if (ind==0) or nums[ind - 1] != num:
                self.twoSum(nums, ind, ans)
        return ans