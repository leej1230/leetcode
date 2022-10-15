class Solution:
    def permutation_recursion(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 1):
            return [nums]
        
        seen = set()

        tmp_ans = []
        for i in range(len(nums)):
            if (nums[i] in seen):
                continue
            else:
                seen.add(nums[i])
                small_permutation = self.permutation_recursion(nums[:i]+nums[i+1:])
                for arr in small_permutation:
                    tmp_ans.append([nums[i]]+arr)
        return tmp_ans

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Recursion Method
        return self.permutation_recursion(nums)

        #Backtracking Method
        res = []
        perm = []
        count = { n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def dfs():
            #Base Case
            if(len(perm) == len(nums)):
                res.append(perm.copy())
                return
            
            for val in count:
                if(count[val] > 0):
                    count[val] -= 1
                    perm.append(val)

                    dfs()

                    count[val] += 1
                    perm.pop()
        dfs()
        return res