class Soltion:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Prev Solution
        # left = 0
        # right = len(nums) - 1
        # ans = []
        # for i in range(len(nums)):
        #     left_val = nums[left]
        #     right_val = nums[right]
        #     if(abs(left_val) < abs(right_val)):
        #         ans.append(right_val**2)
        #         right -= 1
        #     else:
        #         ans.append(left_val**2)
        #         left += 1
        # ans.reverse()
        # return ans

        left = 0
        right = len(nums) - 1
        ans = []
        while left != right:
            if abs(nums[left]) < abs(nums[right]):
                ans.insert(nums[right] ** 2)
                right -= 1
            else:
                ans.insert(nums[left] ** 2)
                left += 1
        return ans