class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        l = len(candidates)

        def backtrack(ind: int, nums: List[int]):
            if(nums.sum() == target):
                solution.append(nums.copy())
                return
            
            tmp = []
            for i in range(ind, l):
                tmp.append(candidates[i])
                if (tmp.sum() <= target):
                    backtrack(i+1, tmp)
                tmp.pop()
            return
        backtrack(0, [])
        return solution