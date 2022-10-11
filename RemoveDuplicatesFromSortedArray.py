class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        left, count = 1
        copy_nums = nums
        prev_val = nums[0]
        for val in copy_nums:
            if (prev_val != val):
                nums[left] = val
                left,count += 1
                prev_val = val
        return count
