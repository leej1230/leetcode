class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(ind, subset):
            if (ind == len(nums)): #Whenever index reaches the end, return it
                res.append(subset.copy())
                return
            
            #Next subset that includes next number no matter what
            subset.append(nums[ind])
            backtrack(ind+1, subset)
            subset.pop() #Reset the subset

            #Next subset that includes next number that is different with previous
            while ind+1 < len(nums) and nums[ind] == nums[ind+1]:
                ind += 1
            backtrack(ind + 1, subset)
        backtrack(0, [])
        return res
