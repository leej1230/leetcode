class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solution = []
        l = len(candidates)

        def backtrack(ind, curr_arr):
            #base case
            if(sum(curr_arr) == target):
                solution.append(curr_arr.copy())
                return
            
            for i in range(ind, l):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                curr_arr.append(candidates[i])
                if sum(curr_arr) <= target:
                    backtrack(i+1, curr_arr)
                curr_arr.pop()
            return
        
        backtrack(0, [])
        return solution