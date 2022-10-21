class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max, prev_min, ans = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            save_max = prev_max
            prev_max = max(x, prev_max*x, prev_min*x)
            prev_min = min(x, save_max*x, prev_min*x)
            ans = max(ans, prev_max)
        return ans