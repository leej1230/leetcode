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
        while left != right:
            if nums[left] ** 2 < nums[right] ** 2:
                pass
            else:
                nums[right], nums[left] = nums[left], nums[right]
            right -= 1
        return [i ** 2 for i in nums]