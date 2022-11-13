class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        d = set()
        while len(nums) > 0:
            a = max(nums)
            b = min(nums)
            nums.remove(a)
            nums.remove(b)
            d.add((a+b)/2)
        return int(len(d))