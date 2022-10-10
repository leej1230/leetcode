class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for val in nums:
            if val not in d:
                d[val] = 0
            else:
                d[val] += 1
        max_freq = -1
        for key,val in d.items():
            if val > max_freq:
                max_freq = val
                solution = key
        return solution