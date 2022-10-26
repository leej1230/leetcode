class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = min(height[left],height[right])*(right - left)
        while left != right:
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
            ans = max(ans, min(height[left],height[right])*(right - left))
        return ans