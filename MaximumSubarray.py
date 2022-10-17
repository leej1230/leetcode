class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        solution = [nums[0]]
        solution_sum = nums[0]
        max_sum = nums[0]
        for x in nums[1:]:
            if(x <= solution_sum+x):
                solution_sum += x
                solution.append(x)
                # if(max_sum < solution_sum):
                #     max_sum = solution_sum
            else:
                solution = [x]
                solution_sum = x
            if(max_sum < solution_sum):
                max_sum = solution_sum
        return max_sum