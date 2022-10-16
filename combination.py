class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [k for k in range(1,n+1)]
        solution = []
        
        def backtrack(ind, num_list):
            if len(num_list) == k:
                solution.append(num_list.copy())
                return
            for i in range(ind, n):
                num_list.append(nums[i])
                backtrack(i+1, num_list)
                num_list.pop()
            return
        
        backtrack(0,[])
        return solution