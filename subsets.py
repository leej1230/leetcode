class Solution:
    def __init__(self):
        self.seen = set()
        self.ans = []
    def recursive_subset(self, nums: List[int]):
        #Base Case
        if(len(nums) == 1 and tuple(nums) not in self.seen):
            self.seen.add(tuple(nums))
            self.ans.append(nums)
            return

        #Recursive Step
        for i in range(len(nums)):
            self.recursive_subset(nums[:i] + nums[i+1:])
        if(tuple(nums) not in self.seen):
            self.seen.add(tuple(nums))
            self.ans.append(nums)
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.recursive_subset(nums)
        if(tuple([]) not in self.seen):
            self.ans.append([])
        return self.ans