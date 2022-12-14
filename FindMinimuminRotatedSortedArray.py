class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer = nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            middle = int((left+right)/2)
            if nums[left] < nums[right]:
                answer = min(answer,nums[left])
                break
            answer = min(answer,nums[middle])
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return answer