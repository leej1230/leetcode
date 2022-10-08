class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        """
        for i in len(nums):
            for k in range(i,len(nums)):
                if nums[i] + nums[k] == target:
                    return [i,k]
        """
        hashmap = {}
        for ind, num in enumerate(nums):
            n = target - num
            if n is in d:
                return(d[n], ind)
            else:
                d[num] = ind
