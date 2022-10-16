class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        solution = []
        nums = [x for x in range(1,10)]
        l = 9

        def backtrack(ind, curr_arr):
            #base case
            if(len(curr_arr) == k):
                if(sum(curr_arr) == n):
                    solution.append(curr_arr.copy())
                return 
            
            for i in range(ind, l):
                curr_arr.append(nums[i])
                if(sum(curr_arr) <= n):
                    backtrack(i+1, curr_arr)
                curr_arr.pop()
            return
        
        backtrack(0, [])
        return solution