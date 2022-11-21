class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        if l==1:
            return False
        sums=set()
        sums.add(0)
        
        target = sum(nums)
        if target%2 != 0:
            return False
        target = target / 2
        
        for i in range(l-1,-1,-1):
            n = nums[i]
            prev = sums.copy()
            for s in sums:
                if s+n == target:
                    return True
                prev.add(s+n)
            sums = prev
        return False

        '''
        The question asks you to find two subsets that has same sum
            In other words, this means, find a sum that exists in array that can be equal to half of sum of array

        So check the array from one end
        add sum to the set of sums that was found so far
        Repeat until the array ends (False) or found the target(half of sum) at somepoint(True)
        '''