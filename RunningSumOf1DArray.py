class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []
        for ind, num in enumerate(nums):
            if ind == 0:
                running.append(num)
            else:
                running.append(num + running[ind - 1])
        return running