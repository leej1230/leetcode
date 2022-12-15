class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left+right)//2
            if target == nums[middle]:
                return middle

            # Check if left < middle
            #   if true, numbers are in right order in left side
            #   compare with middle and move left or right
            elif nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # Else
            #   Numbers are NOT in order
            #   So numbers AFTER middle may contain sorted numbers
        return -1
        '''
        Use binary search
        while left <= right:
            if the target is bigger or equal than left
                if the target is equal to middle return middle
                if the target is smaller than middle change right pointer
                if the target is bigger than middle change left pointer

            if the target is smaller or equal than right
                if the target is equal to middle return middle
                if the target is smaller than middle change right pointer
                if the target is bigger than middle change left pointer
            else return -1
        '''