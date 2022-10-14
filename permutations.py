class Solution:
    def recursive_permute(self, nums: List[int]) -> List[List[int]]:
        tmp_sol = []
        #Base Case
        if(len(nums) == 1):
            return [nums]
        
        #Recursive
        for i in range(len(nums)):
            to_append = self.recursive_permute(nums[:i] + nums[i+1:])
            for arr in to_append:
                tmp_sol.append(nums[i]+arr)
            return tmp_sol

    def permute(self, nums: List[int]) -> List[int]:
        ans = self.recursive_permute(nums)
        return ans