class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for ind, val in enumerate(nums):
            right_sum -= val
            if right_sum == left_sum:
                return ind
            else:
                left_sum += val
        return -1