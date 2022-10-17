class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        subset_sum = sum(nums)/k
        used = [False] * len(nums)

        if(sum(nums)%k != 0):
            return False
        if (len(nums) < k):
            return False
        
        l = len(nums)
        def backtrack(ind, k, sum):
            if (k == 0):
                return True

            if(sum == subset_sum):
                #Build new decision tree from there
                return backtrack(0, k-1, 0)
            
            for i in range(ind, l):
                if used[i] or sum + nums[i] > subset_sum:
                    continue
                used[i] = True
                if backtrack(i+1, k, sum+nums[i]):
                    return True
                used[i] = False

            return False
        return backtrack(0,k,0)